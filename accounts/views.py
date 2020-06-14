from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from accounts.forms import UserLoginForm, UserRegistForm, UserAddressForm
from accounts.models import User, UserAddress
from utils import constants
from utils.verify import VerifyCode


def user_login(request):
    """ User login """
    # If the login is jumped from another page, it will bring next parameter, if there is next parameter, after the login is completed, you need to transfer to
    # The address corresponding to next, otherwise, jump to the home page
    next_url = request.GET.get('next', 'index')
    # First visit URL GET display form for user input
    # Second access to URL POST
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        print(request.POST)
        client = VerifyCode(request)
        code = request.POST.get('vcode', None)
        rest = client.validate_code(code)
        print('Validation results:', rest)
        # Whether the form is verified
        if form.is_valid():
            # Perform login
            data = form.cleaned_data

            # ## Use a custom way to log in
            # # Query user information [MD5] encryption algorithm, irreversible encryption algorithm 1243 -> sdfadfad
            # user = User.objects.get(username=data['username'], password=data['password'])
            # # Set user ID to session
            # request.session[constants.LOGIN_SESSION_ID] = user.id
            # #Jump after login
            # return redirect('index')

            ### Use django-auth to log in
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                # Jump after login
                return redirect(next_url)
        else:
            print(form.errors)
    else:
        form = UserLoginForm(request)
    return render(request, 'login.html', {
        'form': form,
        'next_url': next_url
    })


def user_logout(request):
    """ User logged out """
    logout(request)
    return redirect('index')


def user_register(request):
    """  User registration """
    if request.method == 'POST':
        form = UserRegistForm(request=request, data=request.POST)
        if form.is_valid():
            # Call the registration method
            form.register()
            return redirect('index')
        else:
            print(form.errors)
    else:
        form = UserRegistForm(request=request)
    return render(request, 'register.html', {
        'form': form
    })


@login_required
def address_list(request):
    """ Address list """
    my_addr_list = UserAddress.objects.filter(user=request.user, is_valid=True)
    return render(request, 'address_list.html', {
        'my_addr_list': my_addr_list
    })


@login_required
def address_edit(request, pk):
    """ Add address or edit """
    user = request.user
    addr = None
    initial = {}
    # If PK is a number, it means modification
    if pk.isdigit():
        # Query related address information
        addr = get_object_or_404(UserAddress, pk=pk, user=user, is_valid=True)
        initial['region'] = addr.get_region_format()
    if request.method == 'POST':
        form = UserAddressForm(request=request, data=request.POST,
                               initial=initial, instance=addr)
        if form.is_valid():
            form.save()
            return redirect('accounts:address_list')
    else:
        form = UserAddressForm(request=request, instance=addr, initial=initial)
    return render(request, 'address_edit.html', {
        'form': form
    })


def address_delete(request, pk):
    """ Delete address """
    addr = get_object_or_404(UserAddress, pk=pk, is_valid=True, user=request.user)
    addr.is_valid = False
    addr.save()
    return HttpResponse('ok')

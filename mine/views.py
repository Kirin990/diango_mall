from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum, Q
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView

from mall.models import Product
from mine.models import Order, Cart
from utils import constants, tools


@login_required
def index(request):
    """ Personal Center Homepage """
    return render(request, 'mine.html', {
        'constants': constants
    })


class OrderDetailView(DetailView):
    """ order details """
    model = Order
    slug_field = 'sn'
    slug_url_kwarg = 'sn'
    template_name = 'order_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['constants'] = constants
        return context


@login_required
@transaction.atomic()
def cart_add(request, prod_uid):
    """ Add product to cart Write interface """
    user = request.user
    product = get_object_or_404(Product, uid=prod_uid,
                                is_valid=True,
                                status=constants.PRODUCT_STATUS_SELL)
    # Purchase quantity
    count = int(request.POST.get('count', 1))
    # Check inventory
    if product.ramain_count < count:
        return HttpResponse('no')
    # Reduce inventory
    product.update_store_count(count)
    # Generate shopping cart record
    # If it has been added to the shopping cart, update the purchase quantity and price
    try:
        cart = Cart.objects.get(product=product, user=user,
                                status=constants.ORDER_STATUS_INIT)
        # Update price and quantity
        count = cart.count + count
        cart.count = count
        cart.amount = count * cart.price
        cart.save()
    except Cart.DoesNotExist:
        # Has not been added to the shopping cart
        Cart.objects.create(
            product=product,
            user=user,
            name=product.name,
            img=product.img,
            price=product.price,
            origin_price=product.origin_price,
            count=count,
            amount=count * product.price
        )
    return HttpResponse('ok')


@login_required
def cart(request):
    """ my shopping cart """
    user = request.user
    # List of items in my shopping cart
    prod_list = user.carts.filter(status=constants.ORDER_STATUS_INIT)
    # Aggregate query
    if request.method == 'POST':
        # Submit Order
        # 1.Save a snapshot of the user's address
        default_addr = user.default_addr
        if not default_addr:
            # notification
            messages.warning(request, 'Please select address information')
            return redirect('accounts:address_list')
        # Order total calculation
        cart_total = prod_list.aggregate(sum_amount=Sum('amount'),
                                         sum_count=Sum('count'))
        order = Order.objects.create(
            user=user,
            sn=tools.gen_trans_id(),
            buy_amount=cart_total['sum_amount'],
            buy_count=cart_total['sum_count'],
            to_user=default_addr.username,
            to_area=default_addr.get_region_format(),
            to_address=default_addr.address,
            to_phone=default_addr.phone
        )
        # 2.Modify the status in the cart
        # 3.Generate order, connect to shopping cart
        prod_list.update(
            status=constants.ORDER_STATUS_SUBMIT,
            order=order
        )
        # 4.Jump to order details
        messages.success(request, 'The order is successful, please pay')
        return redirect('mine:order_detail', order.sn)

    return render(request, 'cart.html', {
        'prod_list': prod_list
    })


@login_required
def order_pay(request):
    """ Submit Order """
    user = request.user
    if request.method == 'POST':
        sn = request.POST.get('sn', None)
        # 1.Query order information
        order = get_object_or_404(Order, sn=sn, user=user,
                                  status=constants.ORDER_STATUS_SUBMIT)
        # 2.Verify that the money is enough
        if order.buy_amount > user.integral:
            messages.error(request, 'Insufficient credit balance')
            return redirect('mine:order_detail', sn=sn)
        # 3.Money deducted
        user.ope_integral_account(0, order.buy_amount)
        # 4.Modify order status
        order.status = constants.ORDER_STATUS_PAIED
        order.save()
        # 5.Modify the status of the shopping cart association
        order.carts.all().update(status=constants.ORDER_STATUS_PAIED)
        messages.success(request, 'payment successful')
    return redirect('mine:order_detail', sn=sn)


@login_required
def order_list(request):
    """ My order list """
    status = request.GET.get('status', '')
    try:
        status = int(status)
    except ValueError:
        status = ''
    # 1.Query order data
    # 2.Pagination
    return render(request, 'order_list.html', {
        'constants': constants,
        'status': status
    })


# class-based
class OrderListView(ListView):
    """ Order list based on class view """
    model = Order
    template_name = 'order_list.html'

    def get_queryset(self):
        """ checking order """
        status = self.request.GET.get('status', '')
        user = self.request.user
        query = Q(user=user)
        if status:
            query = query & Q(status=status)
        return Order.objects.filter(query).exclude(
            status=constants.ORDER_STATUS_DELETED
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        status = self.request.GET.get('status', '')
        try:
            status = int(status)
        except ValueError:
            status = ''
        context['constants'] = constants
        context['status'] = status
        return context



@login_required
def prod_collect(request):
    """ my collection """
    return render(request, 'prod_collect.html')

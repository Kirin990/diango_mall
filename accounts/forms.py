import re

from django import forms
from django.contrib.auth import authenticate, login

from accounts.models import User, UserAddress
from utils.verify import VerifyCode


class UserLoginForm(forms.Form):
    """ User login form """
    username = forms.CharField(label='username', max_length=64)
    password = forms.CharField(label='password', max_length=64,
                               widget=forms.PasswordInput,
                               error_messages={
                                   'required': 'Please enter the password'
                               })
    verify_code = forms.CharField(label='Captcha', max_length=4)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # def clean_username(self):
    #     """ 验证用户名 hook 钩子函数"""
    #     username = self.cleaned_data['username']
    #     print(username)
    #     # 判断用户名是否为手机号码
    #     pattern = r'^0{0,1}1[0-9]{10}$'
    #     if not re.search(pattern, username):
    #         raise forms.ValidationError('请输入正确的手机号码')
    #     return username

    def clean_verify_code(self):
        """ Verify that the verification code entered by the user is correct"""
        verify_code = self.cleaned_data['verify_code']
        if not verify_code:
            raise forms.ValidationError('please enter verification code')
        client = VerifyCode(self.request)
        if not client.validate_code(verify_code):
            raise forms.ValidationError('your verification code is not correct')
        return verify_code

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        # username = cleaned_data['username']

        username = cleaned_data.get('username', None)
        password = cleaned_data.get('password', None)
        if username and password:
            # Query users whose username and password match
            user_list = User.objects.filter(username=username)
            if user_list.count() == 0:
                raise forms.ValidationError('Username does not exist')
            # # Verify the password is correct
            # if not user_list.filter(password=password).exists():
            #     raise forms.ValidationError('wrong password')
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('wrong password')
        return cleaned_data


class UserRegistForm(forms.Form):
    """ User registration form """
    username = forms.CharField(label='username', max_length=64)
    nickname = forms.CharField(label='nickname', max_length=64)
    password = forms.CharField(label='password', max_length=64, widget=forms.PasswordInput)
    password_repeat = forms.CharField(label='repeat password', max_length=64, widget=forms.PasswordInput)
    verify_code = forms.CharField(label='verify code', max_length=4)

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean_username(self):
        """ Verify that the user name has been registered """
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError('Username already exists')
        return data

    def clean_verify_code(self):
        """ Verify that the verification code entered by the user is correct"""
        verify_code = self.cleaned_data['verify_code']
        if not verify_code:
            raise forms.ValidationError('please enter verification code')
        client = VerifyCode(self.request)
        if not client.validate_code(verify_code):
            raise forms.ValidationError('your verification code is not correct')
        return verify_code

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password', None)
        password_repeat = cleaned_data.get('password_repeat', None)
        if password and password_repeat:
            if password != password_repeat:
                raise forms.ValidationError('Two password input is inconsistent')
        return cleaned_data

    def register(self):
        """ Registration method """
        data = self.cleaned_data
        # 1.Create user
        User.objects.create_user(username=data['username'],
                                 password=data['password'],
                                 level=0,
                                 nickname='nickname')
        # 2.auto login
        user = authenticate(username=data['username'],
                            password=data['password'])
        login(self.request, user)
        return user


class UserAddressForm(forms.ModelForm):
    """" Add address | Modify"""

    region = forms.CharField(label='Large area options', max_length=64, required=True,
                             error_messages={
                                 'required': 'Please select an address'
                             })

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    class Meta:
        model = UserAddress
        fields = ['address', 'username', 'phone', 'is_default']
        widgets = {
            'is_default': forms.CheckboxInput(attrs={
                'class': 'weui-switch'
            })
        }

    def clean_phone(self):
        """ Verify the mobile number entered by the user """
        phone = self.cleaned_data['phone']
        # Determine if the user name is a mobile phone number
        pattern = r'^0{0,1}1[0-9]{10}$'
        if not re.search(pattern, phone):
            raise forms.ValidationError('Please enter the correct phone number')
        return phone

    def clean(self):
        cleaned_data = super().clean()
        # Query the address data of the currently logged in user
        addr_list = UserAddress.objects.filter(is_valid=True, user=self.request.user)
        if addr_list.count() >= 20:
            raise forms.ValidationError('You can only add up to 20 addresses')
        return cleaned_data

    def save(self, commit=True):
        obj = super().save(commit=False)
        region = self.cleaned_data['region']
        # Provincial data
        (province, city, area) = region.split(' ')
        obj.province = province
        obj.city = city
        obj.area = area
        obj.user = self.request.user

        # When modifying, if there is already a default address, the default address option is currently checked
        # Need to change the previous address to a non-default address
        if self.cleaned_data['is_default']:
            UserAddress.objects.filter(is_valid=True, user=self.request.user,
                                       is_default=True).update(is_default=False)
        obj.save()

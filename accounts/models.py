from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import F


class User(AbstractUser):
    """ User's basic information table """
    # username = models.CharField('User name', max_length=64)
    # password = models.CharField('Password', max_length=255)
    avatar = models.ImageField('User avatar', upload_to='avatar', null=True, blank=True)
    integral = models.IntegerField('User credits', default=0)
    nickname = models.CharField('Nick name', max_length=32)
    level = models.SmallIntegerField('User Level')

    class Meta:
        db_table = 'accounts_user'
        verbose_name = 'Basic information of the user'
        verbose_name_plural = 'Basic information of the user'

    @property
    def default_addr(self):
        """ The user's default address is used in multiple places """
        addr = None
        user_list = self.user_address.filter(is_valid=True)
        # UserAddress.objects.filter(user=user, is_valid=True)
        # 1.Find the default address
        try:
            addr = user_list.filter(is_default=True)[0]
        except IndexError:
            try:
                addr = user_list[0]
                # 2.If there is no default address, display the first of all addresses
            except IndexError:
                pass
        return addr

    def ope_integral_account(self, types, count):
        """ Integral operation """
        if types == 1:
            # Top up
            self.integral = F('integral') + abs(count)
        else:
            # consumption
            self.integral = F('integral') - abs(count)
        self.save()
        self.refresh_from_db()

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    """ User details """
    SEX_CHOICES = (
        (1, 'Male'),
        (0, 'Female'),
    )
    user = models.OneToOneField(User)
    real_name = models.CharField('name', max_length=32)
    email = models.CharField('mailbox', max_length=128, null=True, blank=True)
    is_email_valid = models.BooleanField('mailbox being verified or not', default=False)
    phone_no = models.CharField('phone number', max_length=20, null=True, blank=True)
    is_phone_valid = models.BooleanField('being verified or not', default=False)
    sex = models.SmallIntegerField('sex', default=1, choices=SEX_CHOICES)
    age = models.SmallIntegerField('age', default=0)

    created_at = models.DateTimeField('Create time', auto_now_add=True)
    updated_at = models.DateTimeField('Change time', auto_now=True)

    class Meta:
        db_table = 'accounts_user_profile'
        verbose_name = 'Detailed information of the user'
        verbose_name_plural = 'Detailed information of the user'


class UserAddress(models.Model):
    """ User's address information"""
    user = models.ForeignKey(User, related_name='user_address')
    province = models.CharField('Province', max_length=32)
    city = models.CharField('City', max_length=32)
    area = models.CharField('District', max_length=32)
    town = models.CharField('Street', max_length=32, null=True, blank=True)

    address = models.CharField('Detailed information of the user', max_length=64)
    username = models.CharField('Receiver', max_length=32)
    phone = models.CharField('Receiver phone', max_length=32)

    is_default = models.BooleanField('Whether it is the default address', default=False)
    is_valid = models.BooleanField('Whether it is availabe', default=True)

    created_at = models.DateTimeField('Create time', auto_now_add=True)
    updated_at = models.DateTimeField('Change time', auto_now=True)

    class Meta:
        db_table = 'accounts_user_address'
        verbose_name = 'User address'
        verbose_name_plural = 'User address'
        ordering = ['is_default', '-updated_at']

    def get_phone_format(self):
        """ Format phone number display """
        return self.phone[0:3] + '****' + self.phone[7:]

    def get_region_format(self):
        """ country,city,area"""
        return '{self.province} {self.city} {self.area}'.format(self=self)

    def __str__(self):
        return self.get_region_format() + self.address


class LoginRecord(models.Model):
    """ User's login history """
    user = models.ForeignKey(User)
    username = models.CharField('Log in account', max_length=64)
    ip = models.CharField('IP', max_length=32)
    address = models.CharField('Address', max_length=32, null=True, blank=True)
    source = models.CharField('Source of log in', max_length=32)

    created_at = models.DateTimeField('Log in time')

    class Meta:
        db_table = 'accounts_login_record'
        verbose_name = 'Log in history'
        verbose_name_plural = 'Log in history'


class PasswdChangeLog(models.Model):
    """ User's password modification history """
    pass

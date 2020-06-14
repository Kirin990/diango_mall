from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from accounts.models import User
from mall.models import Product
from system.models import ImageFile
from utils import constants

"""
shopping process
1. View products
2. Add to cart
3. Select the goods in the shopping cart to place an order (choose the delivery address, whether to invoice)
4. Payment
5. Confirm receipt
"""


class Order(models.Model):
    """ Order model """
    sn = models.CharField('Order number', max_length=32)
    user = models.ForeignKey(User, related_name='orders')
    buy_count = models.IntegerField('Purchase quantity', default=1)
    buy_amount = models.FloatField('Total price')

    to_user = models.CharField('Receiver', max_length=32)
    to_area = models.CharField('country', max_length=32)
    to_address = models.CharField('detail address', max_length=256)
    to_phone = models.CharField('phone number', max_length=32)

    remark = models.CharField('remark', max_length=255, null=True, blank=True)

    # 快递信息
    express_type = models.CharField('express delivery', max_length=32, null=True, blank=True)
    express_no = models.CharField('delivery ID', max_length=32, null=True, blank=True)

    status = models.SmallIntegerField('Order Status',
                                      choices=constants.ORDER_STATUS_CHOICES,
                                      default=constants.ORDER_STATUS_SUBMIT)

    class Meta:
        db_table = 'mine_order'
        verbose_name = 'order management'
        verbose_name_plural = 'order management'

    def get_cart_products(self):
        """ Ordered items in the shopping cart """
        # Exclude items still in shopping cart status
        return self.carts.exclude(status=constants.ORDER_STATUS_INIT)


class Cart(models.Model):
    """ shopping cart """
    user = models.ForeignKey(User, related_name='carts')
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order, verbose_name='order', related_name='carts', null=True)
    # 商品快照
    name = models.CharField('product name', max_length=128)
    img = models.ImageField('Main image of the product')
    price = models.IntegerField('Exchange price')
    origin_price = models.FloatField('Original price')

    count = models.PositiveIntegerField('Purchase quantity')
    amount = models.FloatField('total price')

    status = models.SmallIntegerField('status',
                                      choices=constants.ORDER_STATUS_CHOICES,
                                      default=constants.ORDER_STATUS_INIT)

    created_at = models.DateTimeField('create time', auto_now_add=True)
    updated_at = models.DateTimeField('update time', auto_now=True)

    class Meta:
        db_table = 'mine_cart'
        verbose_name = 'shopping cart'
        verbose_name_plural = 'shopping cart'


class Comments(models.Model):
    """ product review """
    # Dimension of rating
    # Anonymous
    # Sticky, sort
    # comments
    # Related pictures
    product = models.ForeignKey(Product, related_name='comments', verbose_name='商品')
    user = models.ForeignKey(User, related_name='comments', verbose_name='用户')
    order = models.ForeignKey(Order, related_name='comments', verbose_name='订单')
    desc = models.CharField('comment content', max_length=256)
    reorder = models.SmallIntegerField('reorder', default=0)
    is_anonymous = models.BooleanField('Is it anonymous', default=True)

    score = models.FloatField('Product Rating', default=10.0)
    score_deliver = models.FloatField('Distribution service scores', default=10.0)
    score_package = models.FloatField('Express packaging scores', default=10.0)
    score_speed = models.FloatField('Delivery speed scores', default=10.0)

    is_valid = models.BooleanField('valid or not', default=True)
    img_list = GenericRelation(ImageFile,
                               verbose_name='comments and show images',
                               related_query_name="img_list")

    created_at = models.DateTimeField('create time', auto_now_add=True)
    updated_at = models.DateTimeField('update time', auto_now=True)

    class Meta:
        db_table = 'mine_product_comments'
        verbose_name = 'product rating'
        verbose_name_plural = 'product rating'

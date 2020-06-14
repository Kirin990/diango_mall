import uuid

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor.fields import RichTextField
from django.db.models import F

from accounts.models import User
from system.models import ImageFile
from utils import constants


class Classify(models.Model):
    """ Classification of goods """
    uid = models.UUIDField('classify_ID', default=uuid.uuid4, editable=True)
    parent = models.ForeignKey('self', related_name='children', null=True, blank=True)
    img = models.ImageField('classify_image', upload_to='classify')
    code = models.CharField('code', max_length=32, null=True, blank=True)
    name = models.CharField('name', max_length=64)
    desc = models.CharField('description', max_length=64, null=True, blank=True)
    reorder = models.SmallIntegerField('reorder', default=0)
    is_valid = models.BooleanField('is_valid', default=True)

    created_at = models.DateTimeField('create_time', auto_now_add=True)
    updated_at = models.DateTimeField('update_time', auto_now=True)

    class Meta:
        db_table = 'mall_classify'
        verbose_name = 'goods_classification'
        verbose_name_plural = 'goods_classification'
        ordering = ['-reorder']

    def __str__(self):
        return '{}:{}'.format(self.code, self.name)


class Tag(models.Model):
    """ Product tags """

    uid = models.UUIDField('tag_id', default=uuid.uuid4, editable=True)
    img = models.ImageField('main_image', upload_to='tags', null=True, blank=True)
    code = models.CharField('code', max_length=32, null=True, blank=True)
    name = models.CharField('name', max_length=12)
    reorder = models.SmallIntegerField('reorder', default=0)
    is_valid = models.BooleanField('is_valid', default=True)

    created_at = models.DateTimeField('create_time', auto_now_add=True)
    updated_at = models.DateTimeField('modify_time', auto_now=True)

    class Meta:
        db_table = 'mall_tag'
        verbose_name = 'product tags'
        verbose_name_plural = 'product tags'
        ordering = ['-reorder']

    def __str__(self):
        return '{}:{}'.format(self.code, self.name)


class Product(models.Model):
    """ product """
    uid = models.UUIDField('product_id', default=uuid.uuid4, editable=False)
    name = models.CharField('product name', max_length=128)
    desc = models.CharField('product description', max_length=256, null=True, blank=True)
    # content = models.TextField('product description')
    # Rich text
    content = RichTextField('product details')

    types = models.SmallIntegerField('product type',
                                     choices=constants.PRODUCT_TYPES_CHOICES,
                                     default=constants.PRODUCT_TYPE_ACTUAL)
    price = models.IntegerField('Exchange price (point exchange)')
    origin_price = models.FloatField('original price')
    img = models.ImageField('main image', upload_to='%Y%m/product')
    buy_link = models.CharField('Purchase link', max_length=256, null=True, blank=True)
    reorder = models.SmallIntegerField('reorder', default=0)
    status = models.SmallIntegerField('Commodity status', default=constants.PRODUCT_STATUS_LOST,
                                      choices=constants.PRODUCT_STATUS_CHOICES)

    sku_count = models.IntegerField('in stock', default=0)
    ramain_count = models.IntegerField('Remaining stock', default=0)
    view_count = models.IntegerField('view count', default=0)
    score = models.FloatField('product rating', default=10.0)

    is_valid = models.BooleanField('is_valid', default=True)

    created_at = models.DateTimeField('create_time', auto_now_add=True)
    updated_at = models.DateTimeField('update_time', auto_now=True)

    tags = models.ManyToManyField(Tag, verbose_name='tags',
                                  related_name='tags',
                                  null=True,
                                  blank=True
                                  )
    classes = models.ManyToManyField(Classify,
                                     verbose_name='classification',
                                     related_name='classes',
                                     null=True,
                                     blank=True)

    banners = GenericRelation(ImageFile, verbose_name='banner image',
                              related_query_name='banners')

    class Meta:
        db_table = 'mall_product'
        verbose_name = 'product information'
        verbose_name_plural = 'product information'
        ordering = ['-reorder']

    def update_store_count(self, count):
        """
        Change product inventory information
        :param count:
        :return:
        """
        self.ramain_count = F('ramain_count') - abs(count)
        self.save()
        self.refresh_from_db()

    def __str__(self):
        return self.name

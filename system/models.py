from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models

from utils import constants


class Slider(models.Model):
    """ System carousel """
    name = models.CharField('name', max_length=32)
    desc = models.CharField('description', max_length=100, null=True, blank=True)
    types = models.SmallIntegerField('position',
                                     choices=constants.SLIDER_TYPES_CHOICES,
                                     default=constants.SLIDER_TYPE_INDEX)
    img = models.ImageField('image', upload_to='slider')
    reorder = models.SmallIntegerField('reorder', default=0, help_text='The higher the number, the higher the front')
    start_time = models.DateTimeField('start_time', null=True, blank=True)
    end_time = models.DateTimeField('end_time', null=True, blank=True)

    target_url = models.CharField('target url', max_length=255, null=True, blank=True)
    is_valid = models.BooleanField('delete or not', default=True)

    created_at = models.DateTimeField('create time', auto_now_add=True)
    updated_at = models.DateTimeField('update time', auto_now=True)

    class Meta:
        db_table = 'system_slider'
        verbose_name = 'slider'
        verbose_name_plural = 'slider'
        ordering = ['-reorder']


class News(models.Model):
    """ news and notification """
    types = models.SmallIntegerField('type', choices=constants.NEWS_TYPES_CHOICES,
                                     default=constants.NEWS_TYPE_NEW)
    title = models.CharField('title', max_length=255)
    content = models.TextField('contents')
    reorder = models.SmallIntegerField('reorder', default=0, help_text='The higher the number, the higher the front')
    start_time = models.DateTimeField('Effective start time', null=True, blank=True)
    end_time = models.DateTimeField('Effective end time', null=True, blank=True)
    view_count = models.IntegerField('views time', default=0)

    is_top = models.BooleanField('Whether to stick', default=False)
    is_valid = models.BooleanField('valid or not', default=True)

    created_at = models.DateTimeField('create time', auto_now_add=True)
    updated_at = models.DateTimeField('update time', auto_now=True)

    class Meta:
        db_table = 'system_news'
        verbose_name = 'news and notification'
        verbose_name_plural = 'news and notification'
        ordering = ['-reorder']


class ImageFile(models.Model):
    """ image """
    # 201902/xxxx
    img = models.ImageField('image_url', upload_to='%Y%m/images/')
    summary = models.CharField('image name', max_length=200)

    # Compound association
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    is_valid = models.BooleanField('valid or not', default=True)

    created_at = models.DateTimeField('create time', auto_now_add=True)
    updated_at = models.DateTimeField('update time', auto_now=True)

    class Meta:
        db_table = 'system_images'
        verbose_name = 'image table'
        verbose_name_plural = 'image table'

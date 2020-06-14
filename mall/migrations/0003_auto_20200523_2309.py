# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-05-23 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0002_delete_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='classify',
            name='code',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='coding'),
        ),
        migrations.AlterField(
            model_name='classify',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='classify',
            name='desc',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='classify',
            name='img',
            field=models.ImageField(upload_to='classify', verbose_name='main_image'),
        ),
        migrations.AlterField(
            model_name='classify',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='valid_or_not'),
        ),
        migrations.AlterField(
            model_name='classify',
            name='name',
            field=models.CharField(max_length=64, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='classify',
            name='reorder',
            field=models.SmallIntegerField(default=0, verbose_name='sort'),
        ),
        migrations.AlterField(
            model_name='classify',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='classification_id'),
        ),
        migrations.AlterField(
            model_name='classify',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='modify_time'),
        ),
        migrations.AlterField(
            model_name='product',
            name='buy_link',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='buy_link'),
        ),
        migrations.AlterField(
            model_name='product',
            name='classes',
            field=models.ManyToManyField(related_name='classes', to='mall.Classify', verbose_name='classifications'),
        ),
        migrations.AlterField(
            model_name='product',
            name='content',
            field=models.TextField(verbose_name='detailed_description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='basic_description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='product', verbose_name='main_image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='valid_or_not'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=128, verbose_name='product_name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='origin_price',
            field=models.FloatField(verbose_name='original_price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='exchange_price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ramain_count',
            field=models.IntegerField(default=0, verbose_name='stock_left'),
        ),
        migrations.AlterField(
            model_name='product',
            name='reorder',
            field=models.SmallIntegerField(default=0, verbose_name='sort'),
        ),
        migrations.AlterField(
            model_name='product',
            name='score',
            field=models.FloatField(default=5.0, verbose_name='score'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku_count',
            field=models.IntegerField(default=0, verbose_name='in_stock'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.SmallIntegerField(choices=[(11, 'on sale'), (12, 'sold out'), (13, 'removed')], default=13, verbose_name='product_status'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='mall.Tag', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='product',
            name='types',
            field=models.SmallIntegerField(choices=[(11, 'Physical_goods'), (12, 'virtual_goods')], default=11, verbose_name='product_type'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='product_id'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='modify_time'),
        ),
        migrations.AlterField(
            model_name='product',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='view_count'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='code',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='coding'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='create_time'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='tags', verbose_name='main_picture'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='valid_or_not'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=12, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='reorder',
            field=models.SmallIntegerField(default=0, verbose_name='sort'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='tags_id'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='modify_time'),
        ),
    ]
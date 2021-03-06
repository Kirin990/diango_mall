# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-05 17:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190504_1305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loginrecord',
            options={'verbose_name': '登录历史', 'verbose_name_plural': '登录历史'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户基础信息', 'verbose_name_plural': '用户基础信息'},
        ),
        migrations.AlterModelOptions(
            name='useraddress',
            options={'ordering': ['is_default', '-updated_at'], 'verbose_name': '用户地址', 'verbose_name_plural': '用户地址'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户详细信息', 'verbose_name_plural': '用户详细信息'},
        ),
    ]

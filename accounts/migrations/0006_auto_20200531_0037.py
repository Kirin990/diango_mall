# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-05-30 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200527_1606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loginrecord',
            options={'verbose_name': 'Log in history', 'verbose_name_plural': 'Log in history'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Basic information of the user', 'verbose_name_plural': 'Basic information of the user'},
        ),
        migrations.AlterModelOptions(
            name='useraddress',
            options={'ordering': ['is_default', '-updated_at'], 'verbose_name': 'User address', 'verbose_name_plural': 'User address'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Detailed information of the user', 'verbose_name_plural': 'Detailed information of the user'},
        ),
        migrations.AlterField(
            model_name='loginrecord',
            name='address',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='loginrecord',
            name='created_at',
            field=models.DateTimeField(verbose_name='Log in time'),
        ),
        migrations.AlterField(
            model_name='loginrecord',
            name='source',
            field=models.CharField(max_length=32, verbose_name='Source of log in'),
        ),
        migrations.AlterField(
            model_name='loginrecord',
            name='username',
            field=models.CharField(max_length=64, verbose_name='Log in account'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar', verbose_name='User avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='integral',
            field=models.IntegerField(default=0, verbose_name='User credits'),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.SmallIntegerField(default=1, verbose_name='User Level'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=32, verbose_name='Nick name'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='address',
            field=models.CharField(max_length=64, verbose_name='Detailed information of the user'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='area',
            field=models.CharField(max_length=32, verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='city',
            field=models.CharField(max_length=32, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create time'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='is_default',
            field=models.BooleanField(default=False, verbose_name='Whether it is the default address'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='is_valid',
            field=models.BooleanField(default=True, verbose_name='Whether it is availabe'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='phone',
            field=models.CharField(max_length=32, verbose_name='Receiver phone'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='province',
            field=models.CharField(max_length=32, verbose_name='Province'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='town',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Street'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Change time'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='username',
            field=models.CharField(max_length=32, verbose_name='Receiver'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.SmallIntegerField(default=0, verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Create time'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='mailbox'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_email_valid',
            field=models.BooleanField(default=False, verbose_name='mailbox being verified or not'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='is_phone_valid',
            field=models.BooleanField(default=False, verbose_name='being verified or not'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone_no',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='real_name',
            field=models.CharField(max_length=32, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.SmallIntegerField(choices=[(1, 'Male'), (0, 'Female')], default=1, verbose_name='sex'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Change time'),
        ),
    ]

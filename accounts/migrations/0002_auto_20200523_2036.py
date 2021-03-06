# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-05-23 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='passowrd',
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=255, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar', verbose_name='profile_picture'),
        ),
        migrations.AlterField(
            model_name='user',
            name='integral',
            field=models.IntegerField(default=0, verbose_name='user_points'),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.SmallIntegerField(verbose_name='user_level'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=32, verbose_name='nickname'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=64, verbose_name='username'),
        ),
    ]

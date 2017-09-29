# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170929_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='authorbio',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]

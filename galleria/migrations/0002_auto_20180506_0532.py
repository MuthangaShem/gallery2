# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='published at'),
        ),
    ]

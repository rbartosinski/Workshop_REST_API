# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20180325_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='screenplay',
        ),
    ]

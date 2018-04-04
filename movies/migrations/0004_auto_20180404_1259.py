# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-04 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movie_screenplay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='starringpersons',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.Movie'),
        ),
        migrations.AlterField(
            model_name='starringpersons',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.Person'),
        ),
    ]

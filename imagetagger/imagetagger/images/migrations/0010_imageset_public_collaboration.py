# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-06 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0009_auto_20171122_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageset',
            name='public_collaboration',
            field=models.BooleanField(default=False),
        ),
    ]

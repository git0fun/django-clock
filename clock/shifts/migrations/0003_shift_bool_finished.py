# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('shifts', '0002_auto_20160606_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='bool_finished',
            field=models.BooleanField(default=False),
        ),
    ]
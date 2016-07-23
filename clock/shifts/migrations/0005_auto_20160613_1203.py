# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-13 10:03
from __future__ import unicode_literals

import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('shifts', '0004_shift_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.',
                                                  through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='shift',
            name='bool_finished',
            field=models.BooleanField(default=False, verbose_name='Shift completed?'),
        ),
    ]
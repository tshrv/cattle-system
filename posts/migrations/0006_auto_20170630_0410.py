# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 22:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20170630_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 30, 4, 10, 26, 771657)),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_modified_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 30, 4, 10, 26, 771603)),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0009_auto_20161012_1919"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="creation_date",
            field=models.DateField(auto_now_add=True, verbose_name="creation date"),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-22 04:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0011_auto_20161014_1901"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"ordering": ["-delivery_date"], "verbose_name_plural": "orders"},
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-02 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0016_auto_20180704_1613"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order_item",
            name="total_quantity",
            field=models.IntegerField(default=0, verbose_name="total quantity"),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("member", "0010_auto_20160803_2052"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="delivery_note",
            field=models.TextField(blank=True, null=True, verbose_name="Delivery Note"),
        ),
    ]

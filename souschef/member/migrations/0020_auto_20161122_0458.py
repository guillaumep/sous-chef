# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-22 04:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0019_auto_20161111_1750"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={
                "ordering": ["-member__created_at"],
                "verbose_name_plural": "clients",
            },
        ),
    ]

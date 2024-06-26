# Generated by Django 1.9.6 on 2016-06-15 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0002_auto_20160614_1736"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="client_order",
                to="member.Client",
                verbose_name="client",
            ),
        ),
    ]

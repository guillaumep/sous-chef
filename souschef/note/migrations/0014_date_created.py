# Generated by Django 1.11.29 on 2021-07-23 15:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("note", "0013_date_modified"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="date_created",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Date Created"
            ),
        ),
    ]

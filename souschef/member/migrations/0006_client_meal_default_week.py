# Generated by Django 1.9.6 on 2016-06-30 15:34

import annoying.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0005_fix004a"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="meal_default_week",
            field=annoying.fields.JSONField(blank=True, null=True),
        ),
    ]

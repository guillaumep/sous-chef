# Generated by Django 1.11.29 on 2021-03-05 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0036_member_addresses"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="address",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="member.Address",
                verbose_name="address",
            ),
        ),
    ]

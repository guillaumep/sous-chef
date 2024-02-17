# Generated by Django 1.10.6 on 2017-03-28 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0030_route_deliveryhistory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client_option",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="member.Client",
                verbose_name="client",
            ),
        ),
        migrations.AlterField(
            model_name="client_option",
            name="option",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="member.Option",
                verbose_name="option",
            ),
        ),
    ]

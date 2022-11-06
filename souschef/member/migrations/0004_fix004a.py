# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-23 01:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("meal", "0002_ingredient_ingredient_group"),
        ("member", "0003_auto_20160615_2100"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client_avoid_component",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Client_avoid_ingredient",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="client_option",
            name="value",
            field=models.CharField(max_length=100, null=True, verbose_name="value"),
        ),
        migrations.AlterField(
            model_name="client",
            name="billing_payment_type",
            field=models.CharField(
                choices=[
                    ("check", "Check"),
                    ("cash", "Cash"),
                    ("debit", "Debit card"),
                    ("credit", "Credit card"),
                    ("eft", "EFT"),
                ],
                max_length=10,
                null=True,
                verbose_name="Payment Type",
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("", "Gender"), ("F", "Female"), ("M", "Male")],
                default="U",
                max_length=1,
                null="True",
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="route",
            field=models.ForeignKey(
                blank=True,
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="member.Route",
                verbose_name="route",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="option",
            name="option_group",
            field=models.CharField(
                choices=[
                    ("main dish size", "Main dish size"),
                    ("dish", "Dish"),
                    ("preparation", "Preparation"),
                    ("other order item", "Other order item"),
                ],
                max_length=100,
                verbose_name="option group",
            ),
        ),
        migrations.AddField(
            model_name="client_avoid_ingredient",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="member.Client",
                verbose_name="client",
            ),
        ),
        migrations.AddField(
            model_name="client_avoid_ingredient",
            name="ingredient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="meal.Ingredient",
                verbose_name="ingredient",
            ),
        ),
        migrations.AddField(
            model_name="client_avoid_component",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="member.Client",
                verbose_name="client",
            ),
        ),
        migrations.AddField(
            model_name="client_avoid_component",
            name="component",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="meal.Component",
                verbose_name="component",
            ),
        ),
    ]

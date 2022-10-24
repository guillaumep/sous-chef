# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-14 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0010_auto_20161012_1921"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("O", "Ordered"),
                    ("D", "Delivered"),
                    ("N", "No Charge"),
                    ("C", "Cancelled"),
                    ("B", "Billed"),
                    ("P", "Paid"),
                ],
                default="O",
                max_length=1,
                verbose_name="order status",
            ),
        ),
        migrations.AlterField(
            model_name="order_item",
            name="component_group",
            field=models.CharField(
                blank=True,
                choices=[
                    ("main_dish", "Main Dish"),
                    ("dessert", "Dessert"),
                    ("diabetic", "Diabetic Dessert"),
                    ("fruit_salad", "Fruit Salad"),
                    ("green_salad", "Green Salad"),
                    ("pudding", "Pudding"),
                    ("compote", "Compote"),
                ],
                max_length=100,
                null=True,
                verbose_name="component group",
            ),
        ),
        migrations.AlterField(
            model_name="order_item",
            name="order_item_type",
            field=models.CharField(
                choices=[
                    (
                        "meal_component",
                        "Meal component (main dish, vegetable, side dish, seasonal)",
                    ),
                    ("delivery", "Delivery (general store item, invitation, ...)"),
                    ("pickup", "Pickup (payment)"),
                    ("visit", "Visit"),
                ],
                max_length=20,
                verbose_name="order item type",
            ),
        ),
        migrations.AlterField(
            model_name="order_item",
            name="remark",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="remark"
            ),
        ),
        migrations.AlterField(
            model_name="order_item",
            name="total_quantity",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="total quantity"
            ),
        ),
    ]

# Generated by Django 1.10 on 2016-12-09 20:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0013_orderstatuschange"),
    ]

    operations = [
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
                    ("sides", "Sides"),
                ],
                max_length=100,
                null=True,
                verbose_name="component group",
            ),
        ),
        migrations.AlterField(
            model_name="order_item",
            name="size",
            field=models.CharField(
                blank=True,
                choices=[("", "Serving size"), ("R", "Regular"), ("L", "Large")],
                max_length=1,
                null=True,
                verbose_name="size",
            ),
        ),
    ]

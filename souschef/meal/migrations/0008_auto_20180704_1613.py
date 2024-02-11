# Generated by Django 1.11.14 on 2018-07-04 20:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meal", "0007_auto_20170313_1442"),
    ]

    operations = [
        migrations.AlterField(
            model_name="component",
            name="component_group",
            field=models.CharField(
                choices=[
                    ("main_dish", "Main Dish"),
                    ("dessert", "Dessert"),
                    ("diabetic", "Diabetic"),
                    ("fruit_salad", "Fruit Salad"),
                    ("green_salad", "Green Salad"),
                    ("pudding", "Pudding"),
                    ("compote", "Compote"),
                    ("sides", "Sides"),
                ],
                max_length=100,
                verbose_name="component group",
            ),
        ),
    ]

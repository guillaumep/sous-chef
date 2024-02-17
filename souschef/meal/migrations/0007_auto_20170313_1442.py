# Generated by Django 1.10.5 on 2017-03-13 18:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meal", "0006_auto_20160826_0007"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="component",
            options={"verbose_name_plural": "components (Dishes and recipes)"},
        ),
        migrations.AlterModelOptions(
            name="restricted_item",
            options={
                "verbose_name_plural": "restricted items (Restriction categories)"
            },
        ),
        migrations.AlterField(
            model_name="component",
            name="component_group",
            field=models.CharField(
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
                verbose_name="component group",
            ),
        ),
    ]

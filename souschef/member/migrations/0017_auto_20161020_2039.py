# Generated by Django 1.10 on 2016-10-20 20:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0016_auto_20160912_1509"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="route",
            options={"ordering": ["name"], "verbose_name_plural": "Routes"},
        ),
        migrations.AlterField(
            model_name="client_option",
            name="value",
            field=models.CharField(max_length=255, null=True, verbose_name="value"),
        ),
    ]

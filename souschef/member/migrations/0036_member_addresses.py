# Generated by Django 1.11.29 on 2021-02-19 16:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0035_auto_20210115_1155"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={
                "ordering": ["number", "street", "apartment"],
                "verbose_name_plural": "addresses",
            },
        ),
        migrations.AlterField(
            model_name="client",
            name="billing_payment_type",
            field=models.CharField(
                blank=True,
                choices=[
                    (" ", "----"),
                    ("3rd", "3rd Party"),
                    ("cash", "Cash"),
                    ("cheque", "Cheque"),
                    ("credit", "Credit card"),
                    ("eft", "EFT"),
                    ("etransfert", "e-Transfer"),
                ],
                max_length=10,
                null=True,
                verbose_name="Payment Type",
            ),
        ),
        migrations.AlterField(
            model_name="member",
            name="address",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="member.Address",
                verbose_name="address",
            ),
        ),
    ]

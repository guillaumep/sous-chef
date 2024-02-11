# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-16 14:31
from __future__ import unicode_literals

from django.db import migrations, models


def set_initial_categories(apps, schema_editor):
    # set NoteCategory initial
    NoteCategory = apps.get_model("note", "NoteCategory")
    NoteCategory.objects.create(name="Follow-up needed")
    NoteCategory.objects.create(name="No Charge")
    NoteCategory.objects.create(name="Orders/Cancellations")
    NoteCategory.objects.create(name="Comments (no actions needed)")
    NoteCategory.objects.create(name="Kitchen Comments")
    NoteCategory.objects.create(name="Stay late notes")
    NoteCategory.objects.create(name="Payment reception")


class Migration(migrations.Migration):
    dependencies = [
        ("note", "0006_change_priority_field"),
    ]

    operations = [
        migrations.CreateModel(
            name="NoteCategory",
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
                ("name", models.CharField(max_length=150, verbose_name="Name")),
            ],
            options={"ordering": ("name",), "verbose_name_plural": "Note categories"},
        ),
        migrations.RunPython(set_initial_categories),
    ]

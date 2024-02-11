# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-16 14:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def set_default_data(apps, schema_editor):
    # set for each product the correct language
    NoteCategory = apps.get_model("note", "NoteCategory")
    Note = apps.get_model("note", "Note")

    default_category = NoteCategory.objects.get(name="Comments (no actions needed)")

    for note in Note.objects.all():
        note.category = default_category
        note.save()


class Migration(migrations.Migration):
    dependencies = [
        ("note", "0007_notecategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notes",
                to="note.NoteCategory",
                verbose_name="Category",
            ),
        ),
        migrations.RunPython(set_default_data),
    ]

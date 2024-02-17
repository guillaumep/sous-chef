# Generated by Django 1.10 on 2017-01-15 04:28

import django.db.models.deletion
from django.db import migrations, models


def migrate_old_data(apps, schema_editor):
    # set for each product the correct language
    NotePriority = apps.get_model("note", "NotePriority")
    Note = apps.get_model("note", "Note")

    normal_priority = NotePriority.objects.get(name="Normal")
    urgent_priority = NotePriority.objects.get(name="Urgent")

    for note in Note.objects.all():
        if note.priority == normal_priority.name.lower():
            note.priority_temp = normal_priority
            note.save()
        elif note.priority == urgent_priority.name.lower():
            note.priority_temp = urgent_priority
            note.save()


class Migration(migrations.Migration):
    dependencies = [
        ("note", "0004_notepriority"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="priority_temp",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="notes",
                to="note.NotePriority",
                verbose_name="Priority",
            ),
        ),
        migrations.RunPython(migrate_old_data),
    ]

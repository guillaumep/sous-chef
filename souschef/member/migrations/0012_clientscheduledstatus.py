# Generated by Django 1.9.8 on 2016-08-17 16:48

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0011_client_delivery_note"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClientScheduledStatus",
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
                (
                    "status_from",
                    models.CharField(
                        choices=[
                            ("D", "Pending"),
                            ("A", "Active"),
                            ("S", "Paused"),
                            ("N", "Stop: no contact"),
                            ("C", "Stop: contact"),
                            ("I", "Deceased"),
                        ],
                        max_length=1,
                    ),
                ),
                (
                    "status_to",
                    models.CharField(
                        choices=[
                            ("D", "Pending"),
                            ("A", "Active"),
                            ("S", "Paused"),
                            ("N", "Stop: no contact"),
                            ("C", "Stop: contact"),
                            ("I", "Deceased"),
                        ],
                        max_length=1,
                    ),
                ),
                ("reason", models.CharField(blank=True, default="", max_length=200)),
                (
                    "change_date",
                    models.DateField(
                        blank=True, default=django.utils.timezone.now, null=True
                    ),
                ),
                (
                    "change_state",
                    models.CharField(
                        choices=[
                            ("ALONE", "Alone"),
                            ("START", "Start"),
                            ("END", "End"),
                        ],
                        default="ALONE",
                        max_length=5,
                    ),
                ),
                (
                    "operation_status",
                    models.CharField(
                        choices=[
                            ("NEW", "To be processed"),
                            ("PRO", "Processed"),
                            ("ERR", "Error"),
                        ],
                        default="NEW",
                        max_length=3,
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="member.Client"
                    ),
                ),
                (
                    "linked_scheduled_status",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="member.ClientScheduledStatus",
                    ),
                ),
            ],
        ),
    ]

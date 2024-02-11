# Generated by Django 1.10.5 on 2017-01-26 16:56

from django.db import migrations, models
import django.db.models.deletion


def migrate_emergency_contacts(apps, schema_editor):
    # set NotePriority initial
    Client = apps.get_model("member", "Client")
    EmergencyContact = apps.get_model("member", "EmergencyContact")
    for client in Client.objects.all():
        if client.emergency_contact:
            EmergencyContact.objects.create(
                client=client,
                member=client.emergency_contact,
                relationship=client.emergency_contact_relationship,
            )


def reverse_emergency_contacts(apps, schema_editor):
    # set NotePriority initial
    Client = apps.get_model("member", "Client")
    EmergencyContact = apps.get_model("member", "EmergencyContact")
    for client in Client.objects.all():
        if client.emergencycontact_set.exists():
            # Use as client emergency contact the first item of
            # relationship
            emergency_contact = client.emergencycontact_set.first()
            # reversing info
            client.emergency_contact = emergency_contact.member
            client.emergency_contact_relationship = emergency_contact.relationship
            client.save()
            # removing info
            EmergencyContact.objects.filter(client=client).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0025_route_vehicle"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmergencyContact",
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
                    "relationship",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="relationship",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "emergency contacts",
            },
        ),
        migrations.AddField(
            model_name="emergencycontact",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="member.Client",
                verbose_name="client",
            ),
        ),
        migrations.AddField(
            model_name="emergencycontact",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="member.Member",
                verbose_name="member",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="emergencycontact",
            unique_together=set([("client", "member")]),
        ),
        migrations.AddField(
            model_name="client",
            name="emergency_contacts",
            field=models.ManyToManyField(
                related_name="emergency_contacts_of",
                through="member.EmergencyContact",
                to="member.Member",
                verbose_name="emergency contacts",
            ),
        ),
        migrations.RunPython(migrate_emergency_contacts, reverse_emergency_contacts),
        migrations.RemoveField(
            model_name="client",
            name="emergency_contact",
        ),
        migrations.RemoveField(
            model_name="client",
            name="emergency_contact_relationship",
        ),
    ]

# Generated by Django 1.10.6 on 2017-04-04 19:56

import django.db.models.deletion
from django.db import migrations, models


def separate_shared_address_instances(apps, schema_editor):
    """
    Before changing ForeignKey to OneToOneField, make sure that members
    use different address instances.
    """
    Member = apps.get_model("member", "Member")
    address_ids = set()
    for m in Member.objects.select_related("address").all():
        a = m.address
        if a is None:
            continue
        if a.pk not in address_ids:
            address_ids.add(a.pk)
            continue
        else:  # a.pk in address_ids
            print(
                "Member #{} ({} {}) shares the Address #{}. I'm copying this "
                "Address instance and relinking the member to it...".format(
                    m.pk, m.firstname, m.lastname, a.pk
                )
            )
            # Copy this object in DB
            a.pk = None
            a.save()
            assert a.pk not in address_ids
            address_ids.add(a.pk)
            m.address = a
            m.save(update_fields=["address"])


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0028_change_linked_scheduled_status_relationship"),
    ]

    operations = [
        migrations.RunPython(
            separate_shared_address_instances, reverse_code=migrations.RunPython.noop
        ),
        migrations.AlterField(
            model_name="member",
            name="address",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="member.Address",
                verbose_name="address",
            ),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-07 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0038_member_verbose_names'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client_cancel_meal_date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancel_date', models.DateField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cancel_meal_dates', to='member.Client', verbose_name='client')),
            ],
        ),
    ]

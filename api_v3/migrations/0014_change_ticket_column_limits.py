# Generated by Django 3.1.7 on 2021-03-28 20:23

import api_v3.models.profile
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v3', '0013_added_expenses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='business_activities',
            field=django_bleach.models.BleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='connections',
            field=django_bleach.models.BleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='initial_information',
            field=django_bleach.models.BleachField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='sources',
            field=django_bleach.models.BleachField(blank=True, null=True),
        ),
    ]
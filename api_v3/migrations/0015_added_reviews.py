# Generated by Django 3.2.4 on 2021-07-06 14:22

from api_v3.models import Review
from django.db import migrations, models
import django.db.models.deletion
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v3', '0014_change_ticket_column_limits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('rating', models.IntegerField(
                    choices=Review.RATINGS,
                    db_index=True,
                    default=0)),
                ('link', models.CharField(max_length=255, null=True)),
                ('body', django_bleach.models.BleachField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='reviews',
                    to='api_v3.ticket')),
            ],
        ),
    ]
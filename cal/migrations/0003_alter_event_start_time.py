# Generated by Django 5.0.1 on 2024-02-22 12:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_alter_event_end_time_alter_event_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

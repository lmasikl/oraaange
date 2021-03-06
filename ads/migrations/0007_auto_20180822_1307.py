# Generated by Django 2.0.8 on 2018-08-22 10:07

import datetime
import django.contrib.postgres.fields
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_auto_20180821_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='viewed_by',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=36), default=list, help_text='View by this users (list of UUIDs).', size=None),
        ),
        migrations.AlterField(
            model_name='ad',
            name='period',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(default=(datetime.datetime(2018, 8, 22, 10, 7, 58, 665186, tzinfo=utc), None), help_text='Ad period'),
        ),
    ]

# Generated by Django 2.0.9 on 2018-11-15 14:37

import ads.models
import django.contrib.postgres.fields.ranges
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0011_auto_20180920_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='period',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(default=ads.models.default_period, help_text='Ad period'),
        ),
    ]

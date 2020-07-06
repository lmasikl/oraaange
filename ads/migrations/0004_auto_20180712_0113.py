# Generated by Django 2.0.7 on 2018-07-11 22:13

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20180709_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='time',
        ),
        migrations.AlterField(
            model_name='ad',
            name='is_active',
            field=models.BooleanField(default=False, help_text='As is publicly published.'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(help_text='Geolocation point (in GeoJSON format).', srid=4326),
        ),
        migrations.AlterField(
            model_name='ad',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'None')], default='N', help_text='Valid values: M, F, N', max_length=1),
        ),
        migrations.AlterField(
            model_name='ad',
            name='text',
            field=models.TextField(help_text='Ad text'),
        ),
    ]

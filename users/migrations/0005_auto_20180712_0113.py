# Generated by Django 2.0.7 on 2018-07-11 22:13

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180711_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=None, help_text='Birtht date.', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='confirm_tos',
            field=models.BooleanField(default=False, help_text='User confirm the offer.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, help_text='Last user location.', null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, help_text='Username.', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'None')], default='N', help_text='Valid Valuesv: M, F, N', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='sms_code',
            field=models.CharField(blank=True, editable=False, help_text='Code from SMS.', max_length=4, null=True),
        ),
    ]
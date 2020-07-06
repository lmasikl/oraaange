# Generated by Django 2.1.4 on 2018-12-26 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0016_ad_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='address',
        ),
        migrations.AlterField(
            model_name='ad',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'None')], default='N', help_text='Valid values: M, F, N', max_length=1),
        ),
    ]
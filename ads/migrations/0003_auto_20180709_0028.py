# Generated by Django 2.0.7 on 2018-07-08 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ad_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='deleted_at',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]

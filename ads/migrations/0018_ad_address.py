# Generated by Django 2.1.4 on 2018-12-26 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0017_auto_20181226_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='address',
            field=models.CharField(default='ul. Mira, 8', help_text='Ad address.', max_length=256),
            preserve_default=False,
        ),
    ]

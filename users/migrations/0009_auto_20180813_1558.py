# Generated by Django 2.0.8 on 2018-08-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_is_self_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.URLField(blank=True, null=True),
        ),
    ]

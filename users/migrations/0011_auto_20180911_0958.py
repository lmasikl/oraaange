# Generated by Django 2.0.8 on 2018-09-11 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_user_is_self_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.UUIDField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.1.5 on 2019-01-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20181212_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='show_activity',
            field=models.BooleanField(default=True, help_text='Show user ativity to others'),
        ),
    ]
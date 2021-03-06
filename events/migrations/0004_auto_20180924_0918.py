# Generated by Django 2.0.8 on 2018-09-24 09:18

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_auto_20180814_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='recipient',
        ),
        migrations.AddField(
            model_name='event',
            name='delivered_to',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=36), default=list, help_text='Event delivered to recipients (list of UUIDs).', size=None),
        ),
        migrations.AddField(
            model_name='event',
            name='recipients',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=36), default=list, help_text='Event recipients (list of UUIDs).', size=None),
        ),
        migrations.AddField(
            model_name='event',
            name='sender',
            field=models.ForeignKey(blank=True, help_text='Event sender.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='payload',
            field=django.contrib.postgres.fields.jsonb.JSONField(help_text='Event data.'),
        ),
    ]

# Generated by Django 2.0.8 on 2018-08-21 14:36

import datetime
from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_ad_is_blocked'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='ages',
            field=django.contrib.postgres.fields.ranges.IntegerRangeField(default=(18, 80), help_text='Ad age range'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ad',
            name='favorited_for',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=36), default=list, help_text='Favorite for this users (list of UUIDs).', size=None),
        ),
        migrations.AddField(
            model_name='ad',
            name='period',
            field=django.contrib.postgres.fields.ranges.DateTimeRangeField(default=(datetime.datetime(2018, 8, 21, 14, 36, 42, 266020, tzinfo=utc), None), help_text='Ad period'),
        ),
        migrations.AddField(
            model_name='ad',
            name='type',
            field=models.CharField(choices=[('ACQUAINTANCE', 'Acquaintance'), ('JOURNEY', 'Journey'), ('MEETING', 'Meeting')], default='ACQUAINTANCE', help_text='Ad type.', max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='user',
            field=models.ForeignKey(help_text='Ad creator.', on_delete=django.db.models.deletion.CASCADE, related_name='ads', to=settings.AUTH_USER_MODEL),
        ),
    ]
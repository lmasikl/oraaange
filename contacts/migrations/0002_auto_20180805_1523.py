# Generated by Django 2.1 on 2018-08-05 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('is_favorite', 'updated_at')},
        ),
        migrations.AddField(
            model_name='contact',
            name='display_name',
            field=models.CharField(blank=True, help_text='Custom contact title.', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.ForeignKey(help_text='User model.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

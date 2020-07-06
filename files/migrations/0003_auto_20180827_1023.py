# Generated by Django 2.0.8 on 2018-08-27 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import files.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '0002_auto_20180709_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.RemoveField(
            model_name='file',
            name='size',
        ),
        migrations.RemoveField(
            model_name='file',
            name='type',
        ),
        migrations.RemoveField(
            model_name='file',
            name='url',
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default='b0be3ea1-0818-4ca7-ba5f-14c2f97e1508', help_text='File object.', upload_to=files.models.rename_to_uuid),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.CharField(choices=[('image', 'Image'), ('video', 'Video'), ('audio', 'Audio'), ('document', 'Document')], default='document', help_text='Valid values: image, video, audio and document.', max_length=8),
        ),
        migrations.AddField(
            model_name='file',
            name='mime_type',
            field=models.CharField(default='application/octet-stream', max_length=32),
        ),
        migrations.AddField(
            model_name='file',
            name='orig_name',
            field=models.CharField(default='README.md', help_text='Original file name.', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='files', to=settings.AUTH_USER_MODEL),
        ),
    ]

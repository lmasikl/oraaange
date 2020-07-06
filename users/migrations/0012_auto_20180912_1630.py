# Generated by Django 2.0.8 on 2018-09-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180911_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'None')], default='N', help_text='Valid Values: M, F, N', max_length=1),
        ),
    ]
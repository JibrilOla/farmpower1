# Generated by Django 4.2.7 on 2023-11-23 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_profile_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='status',
        ),
    ]

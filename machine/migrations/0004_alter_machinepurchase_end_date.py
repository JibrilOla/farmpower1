# Generated by Django 4.2.7 on 2023-11-26 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine', '0003_alter_machinepurchase_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinepurchase',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 10, 52, 21, 738816, tzinfo=datetime.timezone.utc)),
        ),
    ]

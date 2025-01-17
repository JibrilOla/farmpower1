# Generated by Django 4.2.7 on 2023-11-26 15:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_remove_profile_total_rev'),
        ('machine', '0005_remove_machinepurchase_recommending_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='machinepurchase',
            name='recommending_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.profile'),
        ),
        migrations.AddField(
            model_name='machinepurchase',
            name='revenue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='machinepurchase',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 26, 15, 16, 38, 254759, tzinfo=datetime.timezone.utc)),
        ),
    ]

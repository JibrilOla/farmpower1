# Generated by Django 4.2.7 on 2023-11-03 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('withdrawal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdrawal',
            name='date_placed',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

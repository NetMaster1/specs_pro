# Generated by Django 4.1 on 2024-09-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_monitor_reference', '0002_usbport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usbport',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
    ]

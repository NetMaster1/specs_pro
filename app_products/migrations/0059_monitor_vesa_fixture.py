# Generated by Django 4.1 on 2024-09-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0046_vesafixture'),
        ('app_products', '0058_monitor_power_capacity_monitor_usb_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='vesa_fixture',
            field=models.ManyToManyField(blank=True, to='app_reference_shared.vesafixture'),
        ),
    ]

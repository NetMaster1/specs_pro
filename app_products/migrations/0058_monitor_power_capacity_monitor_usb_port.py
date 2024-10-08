# Generated by Django 4.1 on 2024-09-27 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0045_powercapacity'),
        ('app_monitor_reference', '0002_usbport'),
        ('app_products', '0057_monitor_stand_adjustment_monitor_web_camera'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='power_capacity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.powercapacity'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='usb_port',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_monitor_reference.usbport'),
        ),
    ]

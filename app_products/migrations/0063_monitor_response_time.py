# Generated by Django 4.1 on 2024-09-27 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0050_responsetime'),
        ('app_products', '0062_monitor_curved_display_monitor_design_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='response_time',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.responsetime'),
        ),
    ]

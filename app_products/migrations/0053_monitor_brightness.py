# Generated by Django 4.1 on 2024-09-27 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0040_brightness_alter_maxscreenfrequency_is_collection_and_more'),
        ('app_products', '0052_monitor_max_screen_frq'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='brightness',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.brightness'),
        ),
    ]

# Generated by Django 4.1 on 2024-09-30 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0054_hdrstandard'),
        ('app_products', '0069_alter_monitor_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='monitor_connector',
        ),
        migrations.AddField(
            model_name='monitor',
            name='monitor_connector',
            field=models.ManyToManyField(blank=True, to='app_reference_shared.monitorconnector'),
        ),
    ]

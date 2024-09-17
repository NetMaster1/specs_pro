# Generated by Django 4.1 on 2024-09-17 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0002_androidversion_category_dependent_and_more'),
        ('app_products', '0004_remove_smartphone_sensor_smartphone_sensor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='sensor',
        ),
        migrations.AddField(
            model_name='smartphone',
            name='sensor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_reference_shared.sensor'),
        ),
    ]

# Generated by Django 4.1 on 2024-12-19 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0017_alter_maxscreenfrequency_attribute_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TotalSDDVolume',
            new_name='TotalSSDVolume',
        ),
    ]

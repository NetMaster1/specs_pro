# Generated by Django 4.1 on 2024-09-17 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0002_alter_smartphone_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smartphone',
            old_name='Stabilization',
            new_name='stabilization',
        ),
    ]

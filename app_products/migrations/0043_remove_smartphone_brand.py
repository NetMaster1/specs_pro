# Generated by Django 4.1 on 2024-09-24 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0042_remove_smartphone_euro_asian_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='brand',
        ),
    ]

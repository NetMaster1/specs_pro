# Generated by Django 4.1 on 2024-09-21 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0031_alter_smartphone_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='description',
        ),
    ]

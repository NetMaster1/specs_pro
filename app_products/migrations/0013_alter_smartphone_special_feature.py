# Generated by Django 4.1 on 2024-12-14 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0009_specialfeaturesmartphone'),
        ('app_products', '0012_smartphone_model_name_smartphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='special_feature',
            field=models.ManyToManyField(blank=True, to='app_reference_shared.specialfeaturesmartphone'),
        ),
    ]
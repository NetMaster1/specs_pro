# Generated by Django 4.1 on 2024-09-24 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0041_alter_smartphone_part_number_alter_smartphone_type'),
        ('app_reference_smartphones', '0006_brand_is_collection_caseform_is_collection_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brand',
            new_name='BrandSmartphone',
        ),
    ]
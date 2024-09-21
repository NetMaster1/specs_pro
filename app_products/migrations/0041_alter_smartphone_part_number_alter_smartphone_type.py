# Generated by Django 4.1 on 2024-09-21 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0020_json'),
        ('app_reference_smartphones', '0006_brand_is_collection_caseform_is_collection_and_more'),
        ('app_products', '0040_remove_smartphone_interface_smartphone_interface'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='part_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.partnumber'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_reference_smartphones.type'),
        ),
    ]

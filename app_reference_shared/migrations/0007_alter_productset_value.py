# Generated by Django 4.1 on 2024-11-29 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0006_modelname_equipment_brand_modelname_equipment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productset',
            name='value',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]

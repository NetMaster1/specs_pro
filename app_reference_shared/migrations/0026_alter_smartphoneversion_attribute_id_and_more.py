# Generated by Django 4.1 on 2024-09-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0025_rename_operationsystem_osmobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphoneversion',
            name='attribute_id',
            field=models.CharField(blank=True, default='22975', max_length=50),
        ),
        migrations.AlterField(
            model_name='smartphoneversion',
            name='attribute_name',
            field=models.CharField(blank=True, default='Версия смартфона', max_length=50),
        ),
        migrations.AlterField(
            model_name='smartphoneversion',
            name='dictionary_value_id',
            field=models.CharField(blank=True, default='971992309', max_length=20),
        ),
        migrations.AlterField(
            model_name='smartphoneversion',
            name='value',
            field=models.CharField(blank=True, default='Ростест (ЕАС)', max_length=100),
        ),
    ]

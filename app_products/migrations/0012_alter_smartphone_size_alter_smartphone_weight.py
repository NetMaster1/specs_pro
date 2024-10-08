# Generated by Django 4.1 on 2024-09-17 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0005_weight'),
        ('app_products', '0011_smartphone_part_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.size'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='weight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.weight'),
        ),
    ]

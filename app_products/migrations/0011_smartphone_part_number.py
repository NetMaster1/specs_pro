# Generated by Django 4.1 on 2024-09-17 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0003_partnumber'),
        ('app_products', '0010_remove_smartphone_part_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='part_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.partnumber'),
        ),
    ]

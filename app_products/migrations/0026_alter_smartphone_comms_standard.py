# Generated by Django 4.1 on 2024-09-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0013_marketingcolour_processorfrequency_sellercode'),
        ('app_products', '0025_remove_smartphone_authentification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='comms_standard',
            field=models.ManyToManyField(blank=True, to='app_reference_shared.communicationstandard'),
        ),
    ]

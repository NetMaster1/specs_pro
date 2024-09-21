# Generated by Django 4.1 on 2024-09-19 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0013_marketingcolour_processorfrequency_sellercode'),
        ('app_products', '0024_remove_smartphone_charging_function_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='authentification',
        ),
        migrations.AddField(
            model_name='smartphone',
            name='authentification',
            field=models.ManyToManyField(blank=True, to='app_reference_shared.authentication'),
        ),
    ]

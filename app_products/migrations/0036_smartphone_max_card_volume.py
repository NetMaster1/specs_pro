# Generated by Django 4.1 on 2024-09-21 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0019_maxcardvolume'),
        ('app_products', '0035_remove_smartphone_card_max_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='max_card_volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_reference_shared.maxcardvolume'),
        ),
    ]

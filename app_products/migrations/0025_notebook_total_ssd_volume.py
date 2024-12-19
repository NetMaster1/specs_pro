# Generated by Django 4.1 on 2024-12-19 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0018_rename_totalsddvolume_totalssdvolume'),
        ('app_products', '0024_notebook_card_reader_notebook_life_span_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='total_ssd_volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.totalssdvolume'),
        ),
    ]

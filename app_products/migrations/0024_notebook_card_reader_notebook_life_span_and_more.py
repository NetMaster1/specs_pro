# Generated by Django 4.1 on 2024-12-19 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0017_alter_maxscreenfrequency_attribute_name'),
        ('app_products', '0023_notebook_max_screen_frequency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='card_reader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.cardreader'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='life_span',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.lifespan'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='nb_weight',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.notebookweight'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='total_disk_volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.totaldiskvolume'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='total_hdd_volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.totalhddvolume'),
        ),
    ]

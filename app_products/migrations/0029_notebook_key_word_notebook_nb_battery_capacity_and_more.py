# Generated by Django 4.1 on 2024-12-19 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0020_rename_webcamerashutter_webcamshutter'),
        ('app_products', '0028_notebook_keyboard_layout_notebook_keyboard_lightning_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='key_word',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.keyword'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='nb_battery_capacity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.notebookbatterycapacity'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='web_cam_shutter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.webcamshutter'),
        ),
    ]

# Generated by Django 4.1 on 2024-12-23 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_notebook_reference', '0007_rename_notebookinterfacesconnectors_notebookinterfacesconnector'),
        ('app_products', '0030_rename_windwos_version_notebook_windows_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='nb_case_material',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_notebook_reference.notebookcasematerial'),
        ),
    ]
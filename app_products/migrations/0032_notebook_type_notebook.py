# Generated by Django 4.1 on 2024-12-27 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_notebook_reference', '0007_rename_notebookinterfacesconnectors_notebookinterfacesconnector'),
        ('app_products', '0031_notebook_nb_case_material'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='type_notebook',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_notebook_reference.typenotebook'),
        ),
    ]
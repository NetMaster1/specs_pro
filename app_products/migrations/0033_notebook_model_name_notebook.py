# Generated by Django 4.1 on 2024-12-27 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0021_alter_processormodelnotebook_attribute_id'),
        ('app_products', '0032_notebook_type_notebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='model_name_notebook',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.modelname'),
        ),
    ]
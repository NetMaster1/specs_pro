# Generated by Django 4.1 on 2024-12-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0020_rename_webcamerashutter_webcamshutter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processormodelnotebook',
            name='attribute_id',
            field=models.CharField(default='10316', max_length=50),
        ),
    ]
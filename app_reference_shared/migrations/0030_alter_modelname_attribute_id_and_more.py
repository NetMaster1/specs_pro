# Generated by Django 4.1 on 2024-09-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0029_alter_warrantyperiod_attribute_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelname',
            name='attribute_id',
            field=models.CharField(default='9048', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='modelname',
            name='attribute_name',
            field=models.CharField(default='Название модели (для объединения в одну карточку)', max_length=50, null=True),
        ),
    ]

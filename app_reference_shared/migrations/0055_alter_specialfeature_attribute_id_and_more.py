# Generated by Django 4.1 on 2024-10-05 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0054_hdrstandard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialfeature',
            name='attribute_id',
            field=models.CharField(default='5584', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='specialfeature',
            name='attribute_name',
            field=models.CharField(default='Особенности', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='specialfeature',
            name='dictionary_value_id',
            field=models.CharField(default=1, max_length=20),
        ),
    ]

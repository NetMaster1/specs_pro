# Generated by Django 4.1 on 2024-09-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0042_dynamiccontrast_lookangle'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorizontalFrequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Частота горизонтальной развертки, кГц', max_length=50)),
                ('attribute_id', models.CharField(default='5575', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VerticalFrequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Частота вертикальной развертки, Гц', max_length=50)),
                ('attribute_id', models.CharField(default='5576', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
    ]
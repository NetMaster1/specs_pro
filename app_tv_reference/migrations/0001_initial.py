# Generated by Django 4.1 on 2025-01-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandTV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Бренд', max_length=50)),
                ('attribute_id', models.CharField(default='85', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=True)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InteriorTVSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Интерьерный телевизор', max_length=50)),
                ('attribute_id', models.CharField(default='20133', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MediaPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Встроенный медиаплеер', max_length=50)),
                ('attribute_id', models.CharField(default='11526', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SmartTV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Smart TV', max_length=50)),
                ('attribute_id', models.CharField(default='9579', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subwoofer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Сабвуфер', max_length=50)),
                ('attribute_id', models.CharField(default='11523', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVColour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Цвет товара', max_length=50)),
                ('attribute_id', models.CharField(default='10096', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TVCurvedScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Изогнутый экран', max_length=50)),
                ('attribute_id', models.CharField(default='10760', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVDataStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Объем встроенной памяти', max_length=50)),
                ('attribute_id', models.CharField(default='4482', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVHDRTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Технология HDR', max_length=50)),
                ('attribute_id', models.CharField(default='11529', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=True)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVRAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Оперативная память', max_length=50)),
                ('attribute_id', models.CharField(default='4443', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVResolution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Разрешение', max_length=50)),
                ('attribute_id', models.CharField(default='5592', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=True)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVUsb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Количество разъемов USB', max_length=50)),
                ('attribute_id', models.CharField(default='5523', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeTV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Тип', max_length=50)),
                ('attribute_id', models.CharField(default='8229', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=True)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
    ]

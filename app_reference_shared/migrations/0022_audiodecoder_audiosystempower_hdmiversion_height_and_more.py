# Generated by Django 4.1 on 2025-01-06 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0021_alter_processormodelnotebook_attribute_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioDecoder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Декодеры звука', max_length=50)),
                ('attribute_id', models.CharField(default='5179', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=1, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='AudioSystemPower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Мощность аудиосистемы, Вт', max_length=50)),
                ('attribute_id', models.CharField(default='5754', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='HDMIVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Версия HDMI', max_length=50)),
                ('attribute_id', models.CharField(default='11972', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=1, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Height',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Высота, см', max_length=50)),
                ('attribute_id', models.CharField(default='8414', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Сетевые возможности', max_length=50)),
                ('attribute_id', models.CharField(default='11530', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Запись эфира', max_length=50)),
                ('attribute_id', models.CharField(default='11525', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RefreshRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Частота обновления', max_length=50)),
                ('attribute_id', models.CharField(default='5753', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=1, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ResolutionStandard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Стандарт разрешения', max_length=50)),
                ('attribute_id', models.CharField(default='11534', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ScreenTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Технология экрана', max_length=50)),
                ('attribute_id', models.CharField(default='11633', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=1, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SupportSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Размер без подставки (ШxВxГ), мм', max_length=50)),
                ('attribute_id', models.CharField(default='11535', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=1, max_length=20)),
                ('is_required', models.BooleanField(default=True)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVAlternativeModes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Доп. режимы телевизора', max_length=50)),
                ('attribute_id', models.CharField(default='11524', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Управление телевизором', max_length=50)),
                ('attribute_id', models.CharField(default='11527', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TVInterface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Интерфейсы', max_length=50)),
                ('attribute_id', models.CharField(default='11528', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=1, max_length=20)),
                ('is_required', models.BooleanField(default=True)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TVLightningType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Тип подсветки', max_length=50)),
                ('attribute_id', models.CharField(default='11533', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=1, max_length=20)),
                ('is_required', models.BooleanField(default=True)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVMatrixType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Технология матрицы ТВ', max_length=50)),
                ('attribute_id', models.CharField(default='11532', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVOperationSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Операционная система ТВ', max_length=50)),
                ('attribute_id', models.CharField(default='11531', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVPowerConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Мощность, Вт', max_length=50)),
                ('attribute_id', models.CharField(default='4851', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=1, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVScreenSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Диагональ экрана, см', max_length=50)),
                ('attribute_id', models.CharField(default='9227', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TVTuner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='ТВ-тюнер', max_length=50)),
                ('attribute_id', models.CharField(default='5519', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=1, max_length=20)),
                ('is_required', models.BooleanField(default=True)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Width',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Ширина, см', max_length=50)),
                ('attribute_id', models.CharField(default='10175', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='WifiFrequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Частоты Wi-Fi', max_length=50)),
                ('attribute_id', models.CharField(default='5736', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=1, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='interface',
            name='attribute_id',
            field=models.CharField(default='11298', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='interface',
            name='attribute_name',
            field=models.CharField(default='Интерфейсы', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='wirelessinterface',
            name='attribute_id',
            field=models.CharField(default='10387', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='wirelessinterface',
            name='attribute_name',
            field=models.CharField(default='Беспроводные интерфейсы', max_length=50, null=True),
        ),
    ]

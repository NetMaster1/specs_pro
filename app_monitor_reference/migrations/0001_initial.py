# Generated by Django 4.1 on 2024-10-18 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand_Monitor',
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
            name='BuiltinSpeaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Встроенные динамики', max_length=50)),
                ('attribute_id', models.CharField(default='8992', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ColourMonitor',
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
            name='CurvedDispaly',
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
            name='EuroAsianCodeMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='ТН ВЭД коды ЕАЭС', max_length=50)),
                ('attribute_id', models.CharField(default='22232', max_length=50)),
                ('value', models.TextField(blank=True)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='HDR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Технология HDR', max_length=50)),
                ('attribute_id', models.CharField(default='11529', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Resolution',
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
            name='TypeMonitor',
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
        migrations.CreateModel(
            name='USBPort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Количество USB портов', max_length=50)),
                ('attribute_id', models.CharField(default='5727', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default='1', max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
    ]

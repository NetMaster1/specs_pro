# Generated by Django 4.1 on 2024-09-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_monitor_reference', '0003_alter_usbport_is_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuiltinSpeaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Встроенные динамики', max_length=50)),
                ('attribute_id', models.CharField(default='8992', max_length=50)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='usbport',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usbport',
            name='is_required',
            field=models.BooleanField(default=False),
        ),
    ]

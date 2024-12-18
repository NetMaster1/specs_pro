# Generated by Django 4.1 on 2024-12-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_notebook_reference', '0004_rename_ramextraslots_ramextraslot'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotebookProcessorCoreQnty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Число ядер процессора', max_length=50)),
                ('attribute_id', models.CharField(default='10318', max_length=50, null=True)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=1, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=True)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
    ]

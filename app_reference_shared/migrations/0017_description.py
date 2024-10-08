# Generated by Django 4.1 on 2024-09-21 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0016_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Аннотация', max_length=50, null=True)),
                ('attribute_id', models.CharField(default='4191', max_length=50, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('dictionary_value_id', models.CharField(default=0, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=False)),
            ],
        ),
    ]

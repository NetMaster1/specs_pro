# Generated by Django 4.1 on 2024-12-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0008_alter_standadjustment_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialFeatureSmartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(default='Особенности', max_length=50, null=True)),
                ('attribute_id', models.CharField(default='11449', max_length=50, null=True)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('dictionary_value_id', models.CharField(default=1, max_length=20)),
                ('is_required', models.BooleanField(default=False)),
                ('category_dependent', models.BooleanField(default=False)),
                ('is_collection', models.BooleanField(default=True)),
            ],
        ),
    ]

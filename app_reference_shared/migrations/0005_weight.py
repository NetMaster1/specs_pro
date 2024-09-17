# Generated by Django 4.1 on 2024-09-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0004_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=50, null=True)),
                ('attribute_id', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('digital_code', models.CharField(max_length=20)),
                ('is_required', models.BooleanField(default=True)),
                ('category_dependent', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 4.1 on 2024-09-21 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0018_keyword'),
        ('app_products', '0033_smartphone_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smartphone',
            name='marketing_text',
        ),
        migrations.AddField(
            model_name='smartphone',
            name='key_word',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.keyword'),
        ),
    ]

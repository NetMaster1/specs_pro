# Generated by Django 4.1 on 2024-09-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0044_smartphone_card_title_model_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartphone',
            name='image_1',
            field=models.FileField(blank=True, upload_to='uploads'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='image_2',
            field=models.FileField(blank=True, upload_to='uploads'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='image_3',
            field=models.FileField(blank=True, upload_to='uploads'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='image_4',
            field=models.FileField(blank=True, upload_to='uploads'),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='image_5',
            field=models.FileField(blank=True, upload_to='uploads'),
        ),
    ]

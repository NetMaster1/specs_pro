# Generated by Django 4.1 on 2024-09-24 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0045_smartphone_image_1_smartphone_image_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='image_1',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='image_2',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='image_3',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='image_4',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='image_5',
            field=models.URLField(),
        ),
    ]

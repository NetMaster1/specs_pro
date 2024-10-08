# Generated by Django 4.1 on 2024-09-17 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='androidversion',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='authentication',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bluetoothtype',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='camerafunction',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cardtype',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='casematerial',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chargingfunction',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='communicationstandard',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='countryofmanufacture',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='esimsupport',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gadgetserie',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='harddrive',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hazardgrade',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interface',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='iosversion',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='matrixtype',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modelname',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='navigationtype',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='operationsystem',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='processorbrand',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='processormodel',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publishingyear',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ram',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sensor',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='simtype',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='smartphoneversion',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='specialfeature',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stabilization',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videoprocessor',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videoprocessorbrand',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='warrantyperiod',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wifitype',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wirelessinterface',
            name='category_dependent',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.1 on 2024-09-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reference_shared', '0014_rename_name_basiccamerresolution_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='androidversion',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='authentication',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='basiccamerresolution',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='batterycapacity',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bluetoothtype',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='camerafunction',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cardtype',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='casematerial',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='chargingfunction',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='communicationstandard',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='countryofmanufacture',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='esimsupport',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='frontcamerresolution',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gadgetserie',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='harddrive',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hazardgrade',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interface',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='iosversion',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lifespan',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='matrixtype',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modelname',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='navigationtype',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='operationsystem',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='partnumber',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='processorbrand',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='processorfrequency',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='processormodel',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productset',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publishingyear',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ram',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recordmaxspeed',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='screensize',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sellercode',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sensor',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='simtype',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='size',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='smartphoneversion',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='specialfeature',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='stabilization',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='standbyperiod',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videoprocessor',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='videoprocessorbrand',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='warrantyperiod',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='weight',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='wifitype',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='wirelessinterface',
            name='is_collection',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='workperiod',
            name='is_collection',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='marketingcolour',
            name='category_dependent',
            field=models.BooleanField(default=True),
        ),
    ]

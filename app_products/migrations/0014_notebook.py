# Generated by Django 4.1 on 2024-12-18 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_notebook_reference', '0003_keyboardlightning_mobilecommsmodule'),
        ('app_reference_shared', '0013_alter_bluetoothtype_attribute_id_and_more'),
        ('app_products', '0013_alter_smartphone_special_feature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('image_1', models.URLField(blank=True)),
                ('image_2', models.URLField(blank=True)),
                ('image_3', models.URLField(blank=True)),
                ('image_4', models.URLField(blank=True)),
                ('image_5', models.URLField(blank=True)),
                ('battery_capacity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.batterycapacity')),
                ('bluetooth', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_reference_shared.bluetoothtype')),
                ('brand_notebook', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_notebook_reference.brandnotebook')),
                ('category_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.ozoncategory')),
                ('country_of_manufacture', models.ManyToManyField(blank=True, to='app_reference_shared.countryofmanufacture')),
                ('notebook_processor_model', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_reference_shared.processormodelnotebook')),
                ('port_qnty_USB', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_reference_shared.portqntyusb')),
                ('power_off_work_time', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_reference_shared.poweroffworktime')),
                ('product_set', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.productset')),
                ('warranty_period', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.warrantyperiod')),
            ],
            options={
                'verbose_name': 'smartphone',
                'verbose_name_plural': 'smartphones',
            },
        ),
    ]
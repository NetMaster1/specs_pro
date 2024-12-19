# Generated by Django 4.1 on 2024-12-18 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_notebook_reference', '0003_keyboardlightning_mobilecommsmodule'),
        ('app_reference_shared', '0013_alter_bluetoothtype_attribute_id_and_more'),
        ('app_products', '0014_notebook'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='chipset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.chipset'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='hdd_qnty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_notebook_reference.hddqnty'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='notebook_form_factor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.notebookformfactor'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='notebook_max_ram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_notebook_reference.notebookmaxram'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='notebook_ram',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_notebook_reference.ramnotebook'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='notebook_ram_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_notebook_reference.notebookramtype'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='port_usb3_gen1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.portqntyusb3gen1'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='port_usb3_gen2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.portqntyusb3gen2'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='ram_form_factor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_reference_shared.ramformfactor'),
        ),
    ]
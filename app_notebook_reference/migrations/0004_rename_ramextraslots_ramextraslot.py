# Generated by Django 4.1 on 2024-12-19 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0015_notebook_chipset_notebook_hdd_qnty_and_more'),
        ('app_notebook_reference', '0003_keyboardlightning_mobilecommsmodule'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RAMExtraSlots',
            new_name='RAMExtraSlot',
        ),
    ]

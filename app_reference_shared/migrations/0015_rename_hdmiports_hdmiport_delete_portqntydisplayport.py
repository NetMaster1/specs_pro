# Generated by Django 4.1 on 2024-12-19 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0018_delete_notebook'),
        ('app_reference_shared', '0014_delete_portqntyhdmi'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HDMIPorts',
            new_name='HDMIPort',
        ),
        migrations.DeleteModel(
            name='PortQntyDisplayPort',
        ),
    ]
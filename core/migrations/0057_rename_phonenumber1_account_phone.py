# Generated by Django 4.2.6 on 2024-01-11 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_rename_seller_name_account_seller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='phonenumber1',
            new_name='phone',
        ),
    ]

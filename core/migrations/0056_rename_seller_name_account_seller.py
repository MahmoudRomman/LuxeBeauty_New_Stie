# Generated by Django 4.2.6 on 2024-01-11 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_account_seller_name_alter_account_marketer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='seller_name',
            new_name='seller',
        ),
    ]

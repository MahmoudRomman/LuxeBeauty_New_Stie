# Generated by Django 4.2.6 on 2024-01-03 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_account_instagram_account_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='phone',
            new_name='phonenumber',
        ),
    ]

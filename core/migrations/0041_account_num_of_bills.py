# Generated by Django 4.2.6 on 2024-01-08 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_rename_phone_account_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='num_of_bills',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 4.2.6 on 2024-01-13 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_bankaccount_account_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='validation_date',
        ),
    ]

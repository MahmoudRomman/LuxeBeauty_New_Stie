# Generated by Django 4.2.6 on 2024-01-13 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_bankaccount_beneficiary_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='bankaccount',
            name='ccv_or_cvc',
        ),
    ]

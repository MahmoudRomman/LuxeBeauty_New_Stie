# Generated by Django 4.2.6 on 2024-01-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_bankaccount_iban'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='swift_code',
            field=models.CharField(default='15262', max_length=200),
            preserve_default=False,
        ),
    ]

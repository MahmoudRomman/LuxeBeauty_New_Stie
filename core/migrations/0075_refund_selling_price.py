# Generated by Django 4.2.6 on 2024-01-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_bill2_selling_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='refund',
            name='selling_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
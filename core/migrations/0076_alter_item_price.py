# Generated by Django 4.2.6 on 2024-01-24 16:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0075_refund_selling_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=1500, validators=[django.core.validators.MaxValueValidator(15000), django.core.validators.MinValueValidator(50)]),
        ),
    ]
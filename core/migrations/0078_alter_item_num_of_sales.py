# Generated by Django 4.2.6 on 2024-01-28 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0077_rename_offer_offer_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='num_of_sales',
            field=models.PositiveIntegerField(default=1),
        ),
    ]

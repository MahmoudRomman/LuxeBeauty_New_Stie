# Generated by Django 4.2.6 on 2023-11-28 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_bill2_date_alter_order_done_ordered_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='num_of_sales',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bill2',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 11, 52, 13, 571229, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='done_ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 11, 52, 13, 566623, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 11, 52, 13, 566623, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone',
            field=models.CharField(choices=[('1111111111111111', '1111111111111111'), ('222222222222', '222222222222')], max_length=31),
        ),
    ]

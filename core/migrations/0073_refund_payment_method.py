# Generated by Django 4.2.6 on 2024-01-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_bill2_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='refund',
            name='payment_method',
            field=models.CharField(default='tabby', max_length=150),
            preserve_default=False,
        ),
    ]
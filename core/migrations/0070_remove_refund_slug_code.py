# Generated by Django 4.2.6 on 2024-01-18 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_refund_slug_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refund',
            name='slug_code',
        ),
    ]
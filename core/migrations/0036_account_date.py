# Generated by Django 4.2.6 on 2024-01-03 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_rename_account_link_account_tiktok_account_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='date',
            field=models.DateTimeField(default='2023-06-11 23:30:30'),
            preserve_default=False,
        ),
    ]

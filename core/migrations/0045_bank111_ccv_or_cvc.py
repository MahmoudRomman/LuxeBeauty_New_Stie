# Generated by Django 4.2.6 on 2024-01-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_bank111'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank111',
            name='ccv_or_cvc',
            field=models.CharField(default=333, max_length=3),
            preserve_default=False,
        ),
    ]

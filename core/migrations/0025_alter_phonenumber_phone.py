# Generated by Django 4.2.6 on 2023-12-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_phonenumber_phone_delete_phonenumberr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='phone',
            field=models.CharField(choices=[], max_length=31),
        ),
    ]

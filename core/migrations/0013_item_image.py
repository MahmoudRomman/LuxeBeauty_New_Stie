# Generated by Django 4.2.6 on 2023-12-04 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_reward'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='no_product_img.png', null=True, upload_to='core_images'),
        ),
    ]

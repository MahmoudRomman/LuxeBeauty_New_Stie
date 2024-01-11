# Generated by Django 4.2.6 on 2024-01-03 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_account_slug_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='instagram_account_link',
            field=models.URLField(default='http://127.0.0.1:8000/admin/core/account/', max_length=1000),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.6 on 2024-01-09 11:43

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_bill2_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank111',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('card_number', models.CharField(blank=True, max_length=19, null=True)),
                ('validation_date', models.DateField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug_link', models.CharField(max_length=150, unique=True)),
            ],
        ),
    ]
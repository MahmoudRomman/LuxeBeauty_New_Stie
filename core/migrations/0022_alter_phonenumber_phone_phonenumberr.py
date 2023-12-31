# Generated by Django 4.2.6 on 2023-12-27 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0021_alter_phonenumber_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='phone',
            field=models.CharField(choices=[('1111111111111111', '1111111111111111'), ('222222222222', '222222222222'), ('3333333333333333', '3333333333333333'), ('4444444444444444', '4444444444444444')], max_length=31),
        ),
        migrations.CreateModel(
            name='PhoneNumberr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.phones')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2024-01-01 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_phonenumber_phone_phonenumberr'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bill2',
            options={'verbose_name_plural': 'All Bills'},
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.phonenumberr'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='phone',
            field=models.CharField(choices=[('1111111111111111', '1111111111111111'), ('222222222222', '222222222222'), ('3333333333333333', '3333333333333333'), ('4444444444444444', '4444444444444444'), ('55555555555555', '55555555555555'), ('666666666666', '666666666666'), ('77777777777777777', '77777777777777777'), ('88888888888', '88888888888'), ('99999999999999999', '99999999999999999')], max_length=31),
        ),
    ]

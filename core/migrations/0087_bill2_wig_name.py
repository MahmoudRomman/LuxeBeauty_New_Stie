# Generated by Django 4.2.6 on 2024-02-24 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0086_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill2',
            name='wig_name',
            field=models.CharField(choices=[('باروكة شعر طبيعى', 'باروكة شعر طبيعى'), ('مقدمة باروكة شعر طبيعى', 'مقدمة باروكة شعر طبيعى')], default='باروكة شعر طبيعى', max_length=150),
            preserve_default=False,
        ),
    ]
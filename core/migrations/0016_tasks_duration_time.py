# Generated by Django 4.2.6 on 2023-12-19 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_tasks_slug_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='duration_time',
            field=models.DateTimeField(auto_now_add=True, default='2023-12-19 11:02:17.925041+00:00'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.6 on 2024-02-15 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0083_remove_allbillspdf_bill_pdf_allbillspdf_report_pdf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allbillspdf',
            old_name='report_pdf',
            new_name='pdf_file',
        ),
    ]
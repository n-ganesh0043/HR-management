# Generated by Django 2.2.4 on 2020-02-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0002_applicantapllicationmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantapllicationmodel',
            name='ap_percentage',
            field=models.FloatField(),
        ),
    ]
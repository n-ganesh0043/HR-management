# Generated by Django 2.2.4 on 2020-02-19 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitmentm',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='recruitmentm',
            name='responsibilities',
            field=models.CharField(max_length=50),
        ),
    ]

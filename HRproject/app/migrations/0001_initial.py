# Generated by Django 2.2.4 on 2020-02-12 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adminmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Name', models.CharField(max_length=30)),
                ('Password', models.IntegerField()),
                ('Designation', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=40)),
                ('contactno', models.IntegerField(unique=True)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]

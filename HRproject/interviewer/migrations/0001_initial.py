# Generated by Django 2.2.4 on 2020-02-20 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        ('applicant', '0003_auto_20200218_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interviewmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intr_id', models.IntegerField(unique=True)),
                ('sch_date', models.CharField(max_length=20)),
                ('result', models.CharField(max_length=20)),
                ('app_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.ApplicantApllicationModel')),
                ('interviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Adminmodel')),
            ],
        ),
    ]

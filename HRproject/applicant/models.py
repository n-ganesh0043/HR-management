from django.db import models

class Applicantregistrationmodel(models.Model):
    ap_name=models.CharField(max_length=20)
    date_of_birth=models.DateField()
    email_id=models.EmailField()
    gender=models.CharField(max_length=20)
    mobile_no=models.IntegerField(unique=True)
    Address=models.CharField(max_length=20)
    username=models.CharField(unique=True,max_length=20)
    passworD=models.CharField(max_length=20)


class ApplicantApllicationModel(models.Model):
    ap_ap_name=models.CharField(max_length=20)
    ap_date_of_birth=models.DateField()
    ap_email_id=models.EmailField()
    ap_gender=models.CharField(max_length=20)
    ap_mobileno=models.IntegerField(unique=True)
    ap_address=models.CharField(max_length=30)
    ap_post=models.CharField(max_length=30)
    ap_percentage=models.FloatField()
    ap_resume=models.FileField(upload_to='resume_files/')

    def __str__(self):
        return str(self.id)
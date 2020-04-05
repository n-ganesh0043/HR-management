from django.db import models
from applicant.models import ApplicantApllicationModel
from app.models import Adminmodel

class Recruitmentm(models.Model):
    o_code=models.IntegerField(primary_key=True)
    qualification=models.CharField(max_length=30)
    registration_start_from=models.DateField("yy-mm-dd")
    age_limit=models.IntegerField()
    lastdate_to_apply=models.DateField()
    department_id=models.IntegerField()
    no_of_position=models.IntegerField()
    description=models.CharField(max_length=100)
    responsibilities=models.CharField(max_length=50)
    contactno=models.IntegerField(unique=True)


class Interviewerschmodel(models.Model):
    ap_id=models.OneToOneField(ApplicantApllicationModel,on_delete=models.CASCADE,primary_key=True)
    select_emp_id=models.ForeignKey(Adminmodel,on_delete=models.CASCADE)
    date=models.CharField(max_length=20)

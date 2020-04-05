from django.db import models
from applicant.models import ApplicantApllicationModel
from app.models import Adminmodel

class Interviewmodel(models.Model):
    intr_id=models.IntegerField(unique=True)
    interviewer=models.ForeignKey(Adminmodel,on_delete=models.CASCADE)
    sch_date=models.CharField(max_length=20)
    app_id=models.ForeignKey(ApplicantApllicationModel,on_delete=models.CASCADE)
    result=models.CharField(max_length=20)



    def __str__(self):
        return str(self.app_id)



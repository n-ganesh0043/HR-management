from django.db import models

class Adminmodel(models.Model):
    Employee_Name=models.CharField(max_length=30)
    Password=models.IntegerField()
    Designation=models.CharField(max_length=20)
    Address=models.CharField(max_length=40)
    contactno=models.IntegerField(unique=True)
    Email=models.EmailField()
    def __str__(self):
        return str(self.id)
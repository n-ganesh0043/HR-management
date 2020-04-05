from django import forms
from  .models import Interviewmodel

class Interviewform(forms.ModelForm):
    class Meta:
        model=Interviewmodel
        fields="__all__"
from django import forms
from .models import Interviewerschmodel

class Interviewschdform(forms.ModelForm):
    class Meta:
        model=Interviewerschmodel
        fields="__all__"
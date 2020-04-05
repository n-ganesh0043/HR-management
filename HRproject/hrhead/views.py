from django.shortcuts import render,redirect
from django.views.generic import View
from app.models import Adminmodel
from applicant.models import ApplicantApllicationModel
from django.contrib import messages
from interviewer.models import Interviewmodel

class hrhead_login_page(View):
    def get(self,request):
        return render(request,"hrhead/hrhead_login_page.html")
    def post(self,request):
        usr=request.POST.get('bt9')
        psad=request.POST.get('bt10')
        try:
            Adminmodel.objects.get(Email=usr,Password=psad,Designation='HRHEAD')
            return render(request,"hrhead/hrhead_home_page.html")
        except Adminmodel.DoesNotExist:
            messages.success(request,"invalid email or password")
            return redirect('hrhead_login_page')

class hrhead_home_page(View):
    def get(self,request):
        tot = ApplicantApllicationModel.objects.all()
        return render(request, "hrhead/hrhead_home_page.html", {"data": tot})

class view_selected_applicant(View):
    def get(self,request):
        try:
           sel=Interviewmodel.objects.filter(result='selected')
           return render(request,"hrhead/view_selected_applicant.html",{"da1":sel})
        except Interviewmodel.DoesNotExist:
            return redirect("hrhead_home_page")

class view_rejected_applicant(View):
    def get(self,request):
        try:
            sll=Interviewmodel.objects.filter(result='rejected')
            return render(request,"hrhead/view_rejected_applicant.html",{"da2":sll})
        except Interviewmodel.DoesNotExist:
            return redirect("hrhead_home_page")

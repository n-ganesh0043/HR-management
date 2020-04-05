from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .models import Interviewmodel
from applicant.models import ApplicantApllicationModel
from app.models import Adminmodel
from .forms import Interviewform


class interviewer_login_page(View):
    def get(self,request):
        return render(request,"interviewer/interviewer_login_page.html")
    def post(self,request):
        un=request.POST.get('bt7')
        pd=request.POST.get('bt8')
        try:
            e=Adminmodel.objects.get(Email=un,Password=pd,Designation='INTERVIWER')
            ap=ApplicantApllicationModel.objects.values('id')
            return render(request,"interviewer/interviewer_home_page.html",{"data":ap})
        except Adminmodel.DoesNotExist:
            messages.success(request,"INAVALID USERNAME OR PASSWORD!")
            return redirect('interviewer_login_page')

class interviewer_home_page(View):
    def get(self,request):
        print('1')
        ap=ApplicantApllicationModel.objects.values('id')
        print('2')
        print(ap)
        return render(request,"interviewer/interviewer_home_page.html",{"data":ap})
    def post(self,request):
        sf=request.POST.get('w1')
        f=Interviewform
        return render(request,"interviewer/interviewer_main_page.html",{"form":f,"dt":sf})

class interviewer_main_page(View):
    def post(self,request):
        ifm=Interviewform(request.POST)
        if ifm.is_valid():
            ifm.save()
            messages.success(request,"interview date successfully added")
            return render(request,'interviewer/interviewer_main_page.html',{"form":ifm})
        else:
            return render(request,"interviewer/interviewer_home_page.html",{"form":ifm})
    def get(self,request):
        return render(request,"interviewer/interviewer_main_page.html")

def interview_login_page(request):
    ai=ApplicantApllicationModel.objects.get('id')
    return render(request,"interviewer/interviewer_login_page.html",{"data":ai})

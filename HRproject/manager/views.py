from django.shortcuts import render,redirect
from django.views.generic import View,UpdateView,DeleteView,ListView
from .models import Recruitmentm,Interviewerschmodel
from applicant.models import ApplicantApllicationModel
from app.models import Adminmodel
from django.contrib import messages
from manager.forms import Interviewschdform

status="manager"
class manager_home_page(View):
    def get(self,request):
        return render(request,"manager/manager_home_page.html")
    def post(self,request):
        usr=request.POST.get("bt3")
        psd=request.POST.get("bt4")
        if usr=='venky' and psd=='venky123':
            msg="MANAGER login successfully"
            return render(request,"manager/manager_home_page.html",{"message":msg})
        else:
            msg="INVALID username or password.....(TRY AGAIN)!!!!!!"
            return render(request,"manager/manager_login_page.html",{"message":msg})

class add_recruitment_details(View):
    def post(self,request):
        opcd=request.POST.get('fd1')
        qulf=request.POST.get('fd2')
        reg_sr=request.POST.get('fd3')
        agelm=request.POST.get('fd4')
        lstdt=request.POST.get('fd5')
        depid=request.POST.get('fd6')
        npstn=request.POST.get('fd7')
        descp=request.POST.get('fd8')
        resp=request.POST.get('fd9')
        cntct=request.POST.get('fd10')
        Recruitmentm(o_code=opcd,qualification=qulf,registration_start_from=reg_sr,age_limit=agelm,lastdate_to_apply=lstdt,department_id=depid,no_of_position=npstn,description=descp,responsibilities=resp,contactno=cntct).save()
        msg="DETAILS ARE SAVED"
        messages.success(request,msg)
        return redirect('add_recruitment_details')
    def get(self,request):
        return render(request,"manager/add_recruitment_details.html")
class recruitment_modifing_page(View):
    def post(self,request):
        print('1')
        i=request.POST.get("i1")
        print(i)
        try:
          res= Recruitmentm.objects.get(o_code=i)
          print(res)
          return render(request,"manager/recruitment_update_page.html",{"data":res})
        except Recruitmentm.DoesNotExist:
            return render(request,"manager/recruitment_modifing_page.html",{"message":"invalid oppertunity code !!!!!"})
    def get(self,request):
        return render(request,"manager/recruitment_modifing_page.html")

class recruitment_update_page(UpdateView):
    model = Recruitmentm
    fields = "__all__"
    template_name = 'manager/recruitment_update_page.html'
    success_url = '/recruitment_update_page/'
class delete_col(DeleteView):
    model = Recruitmentm
    template_name = 'manager/delete_col.html'
    success_url = '/delete/'

class interview_schd(View):
    def get(self,request):
        ai=ApplicantApllicationModel.objects.values('id')
        return render(request,"manager/interview_schd.html",{"apf":ai})
    def post(self,request):
        aid=request.POST.get('t1')
        ifm=Interviewschdform
        return render(request,"manager/interview_details.html",{"form":ifm,"apf":aid})


class details_saved(View):
    def post(self,request):
        ss=Interviewschdform(request.POST)
        if ss.is_valid():
            ss.save()
            messages.success(request,"successfully added")
            return redirect('details_saved')
        else:
            return render(request,"manager/interview_schd.html")
    def get(self,request):
        return render(request,"manager/interview_details.html")

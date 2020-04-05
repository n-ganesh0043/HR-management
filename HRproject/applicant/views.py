from django.shortcuts import render,redirect
from django.views.generic import View
from .models import Applicantregistrationmodel,ApplicantApllicationModel
from django.contrib import messages

class applicant_login_page(View):
    def get(self,request):
        return render(request,"applicant/applicant_login_page.html")
    def post(self,request):
        usn=request.POST.get('bt5')
        psrd=request.POST.get('bt6')
        try:
          Applicantregistrationmodel.objects.get(username=usn,passworD=psrd)
          return render(request,"applicant/applicant_application_page.html")
        except Applicantregistrationmodel.DoesNotExist:
            messages.success(request,"invalid user")
            return redirect("applicant_login_page")

class applicant_registration_page(View):
    def get(self,request):
        return render(request,"applicant/applicant_registration_page.html")
    def post(self,request):
        n=request.POST.get("ap1")
        dob=request.POST.get("ap2")
        emd=request.POST.get("ap3")
        gen=request.POST.get("ap4")
        mbn=request.POST.get("ap5")
        adr=request.POST.get("ap6")
        usn=request.POST.get("ap7")
        psrd=request.POST.get("ap8")
        Applicantregistrationmodel(ap_name=n,date_of_birth=dob,email_id=emd,gender=gen,mobile_no=mbn,Address=adr,username=usn,passworD=psrd).save()
        messages.success(request,"details are saved")
        return redirect('applicant_registration_page')
class saved_application_details(View):
    def post(self,request):
        n1=request.POST.get('app1')
        dob2=request.POST.get('app2')
        em3=request.POST.get('app3')
        gen4=request.POST.get('app4')
        mb5=request.POST.get('app5')
        ad6=request.POST.get('app6')
        pst7=request.POST.get('app7')
        per=request.POST.get('app8')
        res=request.POST.get('app9')
        ApplicantApllicationModel(ap_ap_name=n1,ap_date_of_birth=dob2,ap_email_id=em3,ap_gender=gen4,ap_mobileno=mb5,ap_address=ad6,ap_post=pst7,ap_percentage=per,ap_resume=res).save()
        messages.success(request,"Applied successfully!!!")
        return render(request,"applicant/applicant_application_page.html")

from django.shortcuts import render,redirect
from django.views.generic import View,ListView,UpdateView,DeleteView
from .models import Adminmodel
from django.contrib import messages
class admin_success(View):
    def post(self,request):
        user=request.POST.get('bt1')
        pswd=request.POST.get('bt2')
        if user=='ganesh' and pswd=='grpspk':
            mess="ADMIN login successfully"
            return render(request,"admin/admin_main_page.html",{"mess":mess})
        else:
            msg='invalid user or password!!!(TRY AGAIN)'
            return render(request,'admin/admin_login_page.html',{"message":msg})
    def get(self,request):
        return render(request,"admin/admin_main_page.html")
class add_employee(View):
    def post(self,request):
        emnm=request.POST.get("em1")
        pswd=request.POST.get('em2')
        desig=request.POST.get('em3')
        adrs=request.POST.get('em4')
        contno=request.POST.get('em5')
        em=request.POST.get('em6')
        Adminmodel(Employee_Name=emnm,Password=pswd,Designation=desig,Address=adrs,contactno=contno,Email=em).save()
        msg="EMPLOYEE SAVED"
        messages.success(request,msg)
        return redirect('add_employee')
    def get(self,request):
        return render(request,"admin/add_employee.html")
class view_all(ListView):
    model = Adminmodel
    template_name ='admin/view_all.html'
    fields="__all__"

class modify_employee(ListView):
    model = Adminmodel
    template_name ='admin/modify.html'

class update_employee(UpdateView):
    model = Adminmodel
    template_name = 'admin/update_employee.html'
    fields = "__all__"
    success_url = '/modify_employee/'

class delete_emplo(DeleteView):
    model = Adminmodel
    template_name = 'admin/delete_emplo.html'
    success_url ='/delete_employee/'


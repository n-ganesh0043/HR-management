"""HRproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView,ListView
from app import views
from app.models import Adminmodel
from manager import urls as m_url
from applicant import urls as ap_url
from interviewer import urls as in_url
from hrhead import urls as hr_url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('admin_login_page/',TemplateView.as_view(template_name='admin/admin_login_page.html'),name="admin_login_page"),
    path('admin_success/',views.admin_success.as_view(),name='admin_success'),
    path('add_employee/',views.add_employee.as_view(),name='add_employee'),
    path('view_all/',views.view_all.as_view(),name='view_all'),
    path('modify_employee/',views.modify_employee.as_view(),name='modify_employee'),
    path('update_employee/<int:pk>',views.update_employee.as_view(),name='update_employee'),
    path('delete_employee/', ListView.as_view(template_name='admin/delete_employee.html', model=Adminmodel), name='delete_employee'),
    path('delete_emplo/<int:pk>',views.delete_emplo.as_view(),name='delete_emplo'),
    path('',include(m_url)),
    path('',include(ap_url)),
    path('',include(in_url)),
    path('',include(hr_url))


]

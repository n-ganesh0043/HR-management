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
from django.urls import path
from django.views.generic import TemplateView,ListView
from manager.models import Recruitmentm
from manager import views

urlpatterns = [
    path('manager_login_page/',TemplateView.as_view(template_name='manager/manager_login_page.html'),name='manager_login_page'),
    path('manager_home_page/',views.manager_home_page.as_view(),name='manager_home_page'),
    path('recruiment/',TemplateView.as_view(template_name='manager/recruimentmenu.html'),name='recruiment'),
    path('add_recruitment_details/',views.add_recruitment_details.as_view(),name='add_recruitment_details'),
    path('recruitment_modifing_page/',views.recruitment_modifing_page.as_view(),name='recruitment_modifing_page'),
    path('recruitment_update_page/<int:pk>',views.recruitment_update_page.as_view(),name='recruitment_update_page'),
    path('delete/',ListView.as_view(template_name='manager/delete_page.html',model=Recruitmentm),name='delete'),
    path('delete_col/<int:pk>',views.delete_col.as_view(),name='delete_col'),
    path('interview_schd/',views.interview_schd.as_view(),name='interview_schd'),
    path('details_saved/',views.details_saved.as_view(),name='details_saved')
]
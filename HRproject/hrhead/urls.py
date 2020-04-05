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
from django.views.generic import TemplateView

from hrhead import views

urlpatterns = [
    path('hrhead_login_page/',views.hrhead_login_page.as_view(),name='hrhead_login_page'),
    path('hrhead_home_page/',views.hrhead_home_page.as_view(),name='hrhead_home_page'),
    path('view_selected_applicant/',views.view_selected_applicant.as_view(),name='view_selected_applicant'),
    path('view_rejected_applicant/',views.view_rejected_applicant.as_view(),name='view_rejected_applicant')
]
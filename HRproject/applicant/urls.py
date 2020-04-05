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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from HRproject import settings
from applicant import views

urlpatterns = [
    path('applicant_login_page/',views.applicant_login_page.as_view(),name='applicant_login_page'),
    path('applicant_registration_page/',views.applicant_registration_page.as_view(),name='applicant_registration_page'),
    path('registration_saved/',views.applicant_registration_page.as_view(),name='registration_saved'),
    path('saved_application_details/',views.saved_application_details.as_view(),name='saved_application_details')
]
if settings.DEBUG:
       urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
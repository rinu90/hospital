"""
URL configuration for hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

from django.urls import path
from . import views

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.register, name='register'),
    path('register/', views.register, name='register'),
      # User type selection page
    path('signup/patient/', views.patient_signup_view, name='patient_signup'),
    path('signup/doctor/', views.doctor_signup_view, name='doctor_signup'),
    path('signin/', views.signin_view, name='signin'),
    path('/dashboard/patient/', views.patient_dashboard_view, name='patient_dashboard'),
    path('dashboard/doctor/', views.doctor_dashboard_view, name='doctor_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



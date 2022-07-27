"""SRS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views             # by me


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.stdlg, name='login page'),
    # path('logout',django.contrib.auth., views.logout_url, name='logout'),
    path('stdlgout', views.stdlgout, name='Student_Login_output'),
    path('_stdlgout_registeredcourse', views._stdlgout_registeredcourse, name='Student_courses in student login page'),
    path('_stdlgout_marks', views._stdlgout_marks, name='Student_marks in student login page'),
  ]
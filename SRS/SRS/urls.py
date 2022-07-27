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
from django.urls import include
from . import views             # by me

urlpatterns = [

    # path('stdlg', views.stdlg, name='Student_Login'),
    # path('stdlgout', views.stdlgout, name='Student_Login_output'),
    # path('_stdlgout_registeredcourse', views._stdlgout_registeredcourse, name='Student_courses in student login page'),
    # path('_stdlgout_marks', views._stdlgout_marks, name='Student_marks in student login page'),
    # path('proflg', views.proflg, name='Professor_Login'),
    # path('admlg', views.admlg, name='admin_Login'),
    # path('proflgout', views.proflgout, name='Professor_Login_output'),
    # path('admlgout', views.admlgout, name='admin_Login_output'),
    # path('signup', views.signup, name='Sign_UP'),
    # path('_admlgout_addstudent', views._admlgout_addstudent, name='Add student in Admin login page'),
    # path('_admlgout_studentlist', views._admlgout_studentlist, name='show students list in Admin login page'),
    # path('_admlgout_proflist', views._admlgout_proflist, name='show professor list in Admin login page'),

    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='ABOUT'),

    path('student/',include('student.urls')),
    path('professor/',include('professor.urls')),
    path('administrator/',include('administrator.urls')),
]

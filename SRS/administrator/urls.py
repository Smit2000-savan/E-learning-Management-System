from django.urls import path
from . import views

urlpatterns=[
    path('',views.admlg,name='login page'),
    path('admlgout',views.admlgout,name='login detail page'),
    path('_admlgout_addstudent', views._admlgout_addstudent, name='Add student in Admin login page'),
    path('_admlgout_studentlist', views._admlgout_studentlist, name='show students list in Admin login page'),
    path('_admlgout_proflist', views._admlgout_proflist, name='show professor list in Admin login page'),

]
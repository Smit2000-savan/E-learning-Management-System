
from django.contrib import admin
from django.urls import path
from . import views             # by me


urlpatterns = [
    path('', views.proflg, name='Login page'),
    path('proflgout', views.proflgout, name='Professor_Login_output'),

]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [path('',views.index,name='home'),
               path('insert/',views.insert,name='next'),
               ]
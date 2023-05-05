from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [path('',views.index,name='home'),
               path('next/',views.next_page,name='next'),]


from django.contrib import admin 
from django.urls import path, include 
from . import views

urlpatterns = [ 
    path('', views.home, name="Hompeage"),
    path('article/<slug:slug>', views.article, name="Article"),
    path('resources', views.resources, name="Resources"),
    path('mosquemap', views.mosquemap, name="MosqueMap"),
    path('community', views.community, name="Community"),
    path('calender', views.calender, name="Calender"),
] 
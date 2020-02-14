
from django.contrib import admin 
from django.urls import path, include 
from . import views

urlpatterns = [ 
    path('', views.home, name="Hompeage"),
    path('article/<slug:post_Slug>', views.article, name="Article"),
    path('resources', views.resources, name="Resources"),
    path('mosquemap', views.mosquemap, name="MosqueMap"),
    path('community', views.community, name="Community"),
    path('calender', views.calender, name="Calender"),

    # Different Category paths
    path('lifestyle', views.lifestyle, name="Lifestyle"),
    path('politics', views.politics, name="Politics"),
    path('opinion', views.opinion, name="Opinion"),
    path('food', views.food, name="Food"),
    path('travel', views.travel, name="Travel"),
    path('health', views.health, name="Health"),
    path('tech', views.tech, name="Tech"),
] 
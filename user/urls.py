from django.urls import include, path
from . import views
from django.contrib import admin


urlpatterns = [
    path('home', views.home, name='home'),
    path('ambulances', views.ambulances, name='ambulances'),
    path('hospitals', views.hospitals, name='user-hospitals'),
    path('first-aid', views.first_aid, name='first-aid')

]

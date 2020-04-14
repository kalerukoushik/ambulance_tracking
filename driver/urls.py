from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('emergency', views.emergency, name='emergency'),
    path('hospitals', views.hospitals, name='hospitals'),
    path('login', views.login, name='login'),
    path('update_status/<int:pk>/', views.update_status, name="update_status")

]


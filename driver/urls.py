from django.urls import include, path
from . import views
from django.contrib import admin

urlpatterns = [
    path('emergency', views.emergency, name='driver-emergency'),
    path('hospitals', views.hospitals, name='driver-hospitals'),
    path('login', views.login, name='driver-login'),
    path('update_status/<int:pk>/', views.update_status, name="update_status")

]


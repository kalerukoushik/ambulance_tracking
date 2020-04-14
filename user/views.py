from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        location= request.POST['location']
        phone= request.POST['phone']
        coordinates = userCoordinates(location= location, phone=phone)
        coordinates.save()
        messages.success(request, 'Coordinates sent successfully')
        return redirect('home')
    else:
        return render(request, 'user/home.html')

def ambulances(request):
    return render(request, 'user/ambulance.html')

def hospitals(request):
    hosp_locations = Hospital.objects.all()
    return render(request, 'user/hospitals.html', {'hosp_locations': hosp_locations})

def first_aid(request):
    return render(request, 'user/first-aid.html')
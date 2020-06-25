from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from user.models import *
from .forms import *
# Create your views here.
def emergency(request):
    locations = userCoordinates.objects.all()
    # locations = sorted(locations.id())
    return render(request, 'driver/emergency.html', {'locations': locations})

def hospitals(request):
    hosp_locations = Hospital.objects.all()
    return render(request, 'driver/hospitals.html', {'hosp_locations': hosp_locations})

def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        # username = Driver.objects.get()

        if Driver.objects.filter(username=username).exists() and Driver.objects.filter(password=password).exists():
            driver = Driver.objects.all()
            return redirect('driver-emergency')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'driver/login.html')

def update_status(request, pk):
    
    status = userCoordinates.objects.get(id=pk)
    
    form = UpdateForm(instance= status)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance = status)
        form.save()
        return redirect('driver-emergency')
    context = {'form': form}
    return render(request, 'driver/update_status.html', context)
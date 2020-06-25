from django.forms import ModelForm
from .models import *
from user.models import *

class UpdateForm(ModelForm):
    class Meta:
        model = userCoordinates
        fields = ['location','description', 'pick_status', 'driver_loc', 'driver_picked']
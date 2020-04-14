from django.forms import ModelForm
from .models import *
from user.models import *

class UpdateForm(ModelForm):
    class Meta:
        model = userCoordinates
        fields = ['location', 'pick_status']
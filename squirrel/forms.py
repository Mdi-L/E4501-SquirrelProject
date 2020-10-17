from django.forms import ModelForm

from .models import Sightings

class sightingForm(ModelForm):
    class Meta:
	model = Sightings
	fields = '__all__'


from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Sightings

def sightings(request):
    all_squrriels_sightings = Sightings.objects.all()
    context = {
            'all_squrriels_sightings': all_squrriels_sightings,
            }
    return render(request, 'squirrel/sightings.html',context)
    

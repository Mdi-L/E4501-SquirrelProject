from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse

from .models import Sightings

sightings = Sightings.objects.all()

def map(request):
#    sightings = Sightings.objects.all()
    context = {
            'sightings':sightings,
            }
    return render(request, 'squirrel/map.html', context)

def list_with_links(request):
    context = {
            'sightings':sightings,
            }
    return render(request, 'squirrel/list_with_links.html', context)

def general_stats(request):
    context = {
            'sightings':sightings,
            }
    return render(request, 'squirrel/general_stats.html', context)

def update(request,input_unique_squirrel_id):
    result = {}
    sighting = get_object_or_404(Sightings, squirrel_unique_id = input_unique_squirrel_id)    
    if request.method == 'POST':
        sighting.latitude = request.POST.get('latitude')
        sighting.longitude = request.POST.get('longigude')
        sighting.unique_squirrel_id = request.POST.get('Unique_squirrel_id')
        sighting.shift = request.POST.get('shift')
        sighting.date = request.POST.get('date')
        sighting.age = request.POST.get('age')
        sighting.save()
        result['statu'] = 'success'
    else:
        result['statu'] = 'error'
    retuen render(request, 'squirrel/update.html', {'result',result})

def create(request):
    result = ''
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longigude')
        unique_squirrel_id = request.POST.get('Unique_squirrel_id')
        shift = request.POST.get('shift')
        date = request.POST.get('date')
        age = request.POST.get('age')
        # need to add other fields
        db = Sightings()
        db.latitude = latitude
        db.longitude = longitude
        db.unique_squirrel_id = unique_squirrel_id
        db.shift = shift
        db.date = date
        db.age = age
        # need to add other fields
        db.save()
        result = 'success'
    return render(request, 'squirrel/create.html', {'result',result})

def detail(request,input_unique_squirrel_id):
    sighting = get_object_or_404(Sightings, squirrel_unique_id = input_unique_squirrel_id)
    context = {
            'sighting':sighting,
            }
    return render(request, 'squirrel/detail.html',context)

# Create your views here.

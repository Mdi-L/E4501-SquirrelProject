
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Sightings
from .forms import sightingForm


def squirrel_gang(request):
    return render(request, 'squirrel/squirrel_gang.html')

def map_(request):
    sightings = Sightings.objects.all()
	
    context = {
            'sightings' : sightings[:99]
            }
	
    return render(request, 'squirrel/map.html', context)


def sightings(request):
    allsightings = Sightings.objects.all()
    
    context = {
            'allsightings': allsightings,
           }
    
    return render(request, 'squirrel/sightings.html',context)


	
def update(request,unique_squirrel_id):

    if request.method == 'POST':
        sighting = Sightings.objects.get(unique_squirrel_id=unique_squirrel_id)
        form = sightingForm(request.POST, instance = sighting)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/{unique_squirrel_id}')
    else:
        sighting = Sightings.objects.get(unique_squirrel_id=unique_squirrel_id)
        form = sightingForm(instance = sighting)
	
    context = {
            'form': form
            }
		
    return render(request, 'squirrel/update.html', context)
	

def add(request):
    if request.method == 'POST':
        form = sightingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = sightingForm()
	
    context = {
            'form': form
            }
		
    return render(request, 'squirrel/add.html', context)


def stats(request):
    allsightings = Sightings.objects.all()
    # general summary
    total_count = allsightings.count(),
    # specific summary
    # shift
    AM_count = allsightings.filter(shift = 'AM').count()
    PM_count = allsightings.filter(shift = 'PM').count()
    AM_ratio = "{:.2%}".format(AM_count/(AM_count+PM_count))
    PM_ratio = "{:.2%}".format(PM_count/(AM_count+PM_count))
    # age
    Adult_count = allsightings.filter(age = 'Adult').count()
    Juvenile_count = allsightings.filter(age = 'Juvenile').count()
    Adult_ratio = "{:.2%}".format(Adult_count/(Adult_count+Juvenile_count))
    Juvenile_ratio = "{:.2%}".format(Juvenile_count/(Adult_count+Juvenile_count))
    # primary_fur_color 
    Gray_count = allsightings.filter(primary_fur_color = 'Gray').count()
    Cinnamon_count = allsightings.filter(primary_fur_color = 'Cinnamon').count()
    Black_count = allsightings.filter(primary_fur_color = 'Black').count()
    fur_sum = Gray_count + Cinnamon_count + Black_count
    Gray_ratio = "{:.2%}".format(Gray_count/fur_sum)
    Cinnamon_ratio = "{:.2%}".format(Cinnamon_count/fur_sum)
    Black_ratio = "{:.2%}".format(Black_count/fur_sum)
    # location
    AG_count = allsightings.filter(location  = 'Above Ground').count()
    GP_count = allsightings.filter(location  = 'Ground Plane').count()
    AG_ratio = "{:.2%}".format(AG_count/(AG_count+GP_count))
    GP_ratio = "{:.2%}".format(GP_count/(AG_count+GP_count))

    context = {
	'total_count' : total_count[0],
	'shift' : {'AM_count': AM_count, 'PM_count':PM_count},
	'shift_ratio' : {'AM_ratio': AM_ratio, 'PM_ratio':PM_ratio},
	'age' : {'Adult_count': Adult_count, 'Juvenile_count':Juvenile_count},
	'age_ratio' : {'Adult_ratio': Adult_ratio, 'Juvenile_ratio':Juvenile_ratio},
	'primary_fur_color' : {'Gray_count': Gray_count,'Cinnamon_count':Cinnamon_count, 'Black_count':Black_count},
	'primary_fur_color_ratio' : {'Gray_ratio': Gray_ratio,'Cinnamon_ratio':Cinnamon_ratio, 'Black_ratio':Black_ratio},
	'location' : {'AG_count': AG_count, 'GP_count':GP_count},
	'location_ratio' : {'AG_ratio': AG_ratio, 'GP_ratio':GP_ratio},
	}

    return render(request, 'squirrel/stats.html',context)







    

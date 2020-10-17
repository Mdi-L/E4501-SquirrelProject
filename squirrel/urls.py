from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'squirrel'

urlpatterns = [

    path('squirrelhub/', views.squirrel_gang, name='squirrel_gang'),
    path('map/', views.map_, name='map'),
    path('sightings/', views.sightings, name='all'),
    path('sightings/<unique_squirrel_id>/', views.update, name='update'),
    path('sightings/add/', views.add, name='add'),
    path('sightings/stats/', views.stats, name='stats'),
    ]

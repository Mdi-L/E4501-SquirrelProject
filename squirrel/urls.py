from django.urls import path

from . import views

app_name = 'squirrel'

urlpatterns = [
        path('map', views.map)
        path('sightings', views.list_with_links, name='list'),
        path('sightings/<int:input_unique_squirrel_id>/', views.update),
        path('sightings/add/', views.create, name='create'),
        path('sightings/stats/', views.general_stats, name='stats'),
        path('sightings/detail/<int:input_unique_squirrel_id>/', views.detail, name='detail'),
        ]

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, LabelCommand, CommandError
from squirrel.models import Sightings
import csv


class Command(LabelCommand):
    
    def handle_label(self, label, **options):

        data=csv.reader(open(label), delimiter=',', quotechar='"')
        for row in data:
    	    Sightings.objects.update_or_create(
  	        latitude = row[0],
    	    	longitude = row[1],
            	unique_squirrel_id = row[2],
                shift = row[4],
		date = row[5],
		age = row[7],
    	        primary_fur_color = row[8],
       	        location = row[12],
    	        specifi_location = row[14],
	        running = row[15],
    	        chasing = row[16],
    	        climbing = row[17],
    	        eating = row[18],
                foraging = row[19],
	        other_activities = row[20],
                kuks = row[21],
                quaas = row[22],
    	        moans = row[23],
    	        tail_flags = row[24],
                tail_twitches = row[25],
	        # approaches = row[26],
                indifferent = row[27],
                runs_from = row[28]
            )	
        self.stdout.write(self.style.SUCCESS('Data has been imported from %s' % (label)))

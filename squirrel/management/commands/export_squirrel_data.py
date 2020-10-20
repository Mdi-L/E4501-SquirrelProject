from django.core.management.base import BaseCommand
from squirrel.models import Sightings
import datetime
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
    	parser.add_argument('file_path')

    def handle(self, *args, **options):
        path = options['file_path']
        columns_ = ['X','Y','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color','Location','Specific Location',                   'Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans',
                  'Tail flags','Tail twitches','Approaches','Indifferent','Runs from']
        
        with open(path,'w') as fp:
            export_ = csv.DictWriter(fp, delimiter=',',fieldnames=columns_)
            export_.writeheader()

            for row in Sightings.objects.all():
                context = {
                        'X':row.latitude,
                        'Y':row.longitude,
                        'Unique Squirrel ID':row.unique_squirrel_id,
                        'Shift':row.shift,
                        'Date':row.date,
                        'Age':row.age,
                        'Primary Fur Color':row.primary_fur_color,
                        'Location':row.location,
                        'Specific Location':row.specific_location,
                        'Running':row.running,
                        'Chasing':row.chasing,
                        'Climbing':row.climbing,
                        'Eating':row.eating,
                        'Foraging':row.foraging,
                        'Other Activities':row.other_activities,
                        'Kuks':row.kuks,
                        'Quaas':row.quaas,
                        'Moans':row.moans,
                        'Tail flags':row.tail_flags,
                        'Tail twitches':row.tail_twitches,
                        'Approaches':row.approaches,
                        'Indifferent':row.indifferent,
                        'Runs from':row.runs_from
			}
                export_.writerow(context)

            self.stdout.write(self.style.SUCCESS('Data has been exported to %s' % (path)))

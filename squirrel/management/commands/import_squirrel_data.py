from django.core.management.base import BaseCommand
from squirrel.models import Sightings
import datetime
import csv


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path')

    def handle(self, *args, **options):
        path = options['file_path']

        with open(path) as fp:
            data=csv.DictReader(fp)

        def trans_bool(origin):
            return str(origin).lower() == 'true'
			
            for row in data:
    
                Sightings.objects.get_or_create(
                        latitude = float(row[0]),
                        longitude = float(row[1]),
                        unique_squirrel_id = row[2],
                        shift = row[4],
                        date = datetime.date(int(row[5][-4:]), int(row[5][:2]), int(row[5][2:4])),
                        age = row[7],

                        primary_fur_color = row[8],
                        location = row[12],
                        specific_location = row[14],
                        running = trans_bool(row[15]),
                        chasing = trans_bool(row[16]),
                        climbing = trans_bool(row[17]),
                        eating = trans_bool(row[18]),
                        foraging = trans_bool(row[19]),
                        other_activities = row[20],
                        kuks = trans_bool(row[21]),
                        quaas = trans_bool(row[22]),
                        moans = trans_bool(row[23]),
                        tail_flags = trans_bool(row[24]),
                        tail_twitches = trans_bool(row[25]),
                        approaches = trans_bool(row[26]),
                        indifferent = trans_bool(row[27]),
                        runs_from = trans_bool(row[28]),
                        )

        self.stdout.write(self.style.SUCCESS('Data has been imported from %s' % (path)))

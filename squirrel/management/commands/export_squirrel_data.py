#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError

import csv

class Command(BaseCommand):
    
    def add_arguments(self, parser):

        parser.add_argument(
            'pathToExData'
            help = 'the path to export  csv file'
                
        )
        
    def handle(self, *args):
        try:
            csvfile = open(args['pathToExData'],'wb')
            writer = csv.writer(csvfile)
            writer.writerrow(['column1','column2'])
            data = [
                (),
                ()

             ]

            writer.writerows(data)

            csvfile.close

            self.stdout.write(self.style.SUCCESS('Data has been successfully exported to %s' % (args['pathToExData'])))
            
        except Exception as ex:
            self.stdout.write(self.style.ERROR('Erro in export data'))

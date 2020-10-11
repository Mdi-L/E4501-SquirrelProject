#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError

import csv

class Command(BaseCommand):
    
    def add_arguments(self, parser):

        parser.add_argument(
            'pathToImData',
            help = 'the path to import  csv file'

        )

    def handle(self, **args):
        try:
            with open(args['pathToImData'],'rb') as myData:   
                data=csv.reader(myData)

            self.stdout.write(self.style.SUCCESS('Data has been successfully imported from %s' % (args['pathToImData'])))

        except Exception as ex:
            self.stdout.write(self.style.ERROR('Error in import data'))



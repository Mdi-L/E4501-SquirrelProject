from django.db import models

class Sightings(models.Model):
    latitude = models.DecimalField(
            max_digits=5, 
            decimal_places=2
            )

    longitude = models.DecimalField(
            max_digits=5,
            decimal_places=2
            )

    unique_squirrel_id = models.CharField(
            max_length = 15,
            )

    AM='AM'
    PM='PM'
    ShiftChoice = ((AM,'AM'),(PM,'PM'))
    shift = models.CharField(
            max_length = 2,
            choices = ShiftChoice
            )

    date = models.DateField()
    
    Adult = 'Adult'
    Juvenile = 'Juvenile'
    AgeChoice = ((Adult,'Adult'),(Juvenile,'Juvenile'))
    age = models.CharField(
            max_length = 15,
            choices = AgeChoice,
            blank = True,
            )
    
    primary_fur_color = models.CharField(
            max_length = 20,
            blank = True,
            )

    location = models.CharField(
            max_length = 20,
            blank = True,
            )

    specific_location = models.TextField(
            blank = True
            )

    running = models.BooleanField()

    chasing = models.BooleanField()

    climbing = models.BooleanField()

    eating = models.BooleanField()

    foraging = models.BooleanField()

    other_activities = models.TextField(
            blank = True,
            )

    kuks = models.BooleanField()

    quaas = models.BooleanField()           

    moans = models.BooleanField()

    tail_flags = models.BooleanField()
    
    tail_twitches = models.BooleanField()

    approaches = models.BooleanField()
    
    runs_from = models.BooleanField()

# Create your models here.

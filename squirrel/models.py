
from django.db  import models
from django.utils.translation import gettext as _

class Sightings(models.Model):

    latitude = models.FloatField(
                max_length = 20,
		help_text = _('latitude')
		)

    longitude = models.FloatField(
                max_length = 20,
		help_text = _('longitude')
		)

    unique_squirrel_id = models.CharField(
		max_length = 15,
		help_text = _('unique_squirrel_id')
		)
	
    AM = 'AM'
    PM = 'PM'
    shift_choice = ((AM,'AM'),(PM,'PM'),)
    shift = models.CharField(
		max_length = 2,
                choices = shift_choice,
                blank = True,
                null = True,
		help_text = _('shift: AM? PM? leave it blank if do not known')
		)

    date = models.DateField(
                help_text = _('date:xxxx-xx-xx')
		)

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    age_choice = ((Adult,'Adult'),(Juvenile,'Juvenile'))
    age = models.CharField(
		max_length = 20,
                choices = age_choice,
		blank = True,
		null = True,
		help_text = _('age: Adult? Juvenile? leave it blank if do not known')
		)
    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Black = 'Black'
    fcolor_choice = ((Gray,'Gray'),(Cinnamon,'Cinnamon'),(Black,'Black'))
    primary_fur_color = models.CharField(
		max_length = 20,
                choices = fcolor_choice,
		blank = True,
		null = True,
		help_text = _('primary fur color: Gray? Cinnamon? Black? leave it blank if do not known')
		)

    AG = 'Above Ground'
    GP = 'Ground Plane'
    l_choice = ((AG,'Above Ground'),(GP,'Ground Plane'))
    location = models.CharField(
		max_length = 50,
                choices = l_choice,
		blank = True,
		null = True,
		help_text = _('location: Above Ground? Ground Plane? leave it blank if do not known')
		)

    specific_location = models.CharField(
		max_length = 200,
		blank = True,
		null = True,
		help_text = _('specific location, leave it blank if do not known')
		)

    running = models.BooleanField(
		default = False,
		help_text = _('running?')
		)

    chasing = models.BooleanField(
		default = False,
		help_text = _('chasing?')
		)

    climbing = models.BooleanField(
		default = False,
		help_text = _('climbing?')
		)

    eating = models.BooleanField(
		default = False,
		help_text = _('eating?')
		)

    foraging = models.BooleanField(
		default = False,
		help_text = _('foraging?')
		)

    other_activities = models.CharField(
		max_length = 200,
		blank = True,
		null = True,
		help_text = _('other_activities')
		)
			
    kuks = models.BooleanField(
		default = False,
		help_text = _('kuks?')
		)
		
    quaas = models.BooleanField(
		default = False,
		help_text = _('quaas?')
		)
		
    moans = models.BooleanField(
		default = False,
		help_text = _('moans?')
		)
		
    tail_flags = models.BooleanField(
		default = False,
		help_text = _('tail flags?')
		)
		
    tail_twitches = models.BooleanField(
		default = False,
		help_text = _('tail twitches?')
		)
		
    approaches = models.BooleanField(
		default = False,
		help_text = _('approaches?')
		)
		
    indifferent = models.BooleanField(
		default = False,
		help_text = _('indifferent?')
		)
		
    runs_from = models.BooleanField(
		default = False,
		help_text = _('runs from?')
		)

    def __str__(self):
        return self.name

			

# Create your models here.

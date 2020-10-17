
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
	
    shift = models.CharField(
		max_length = 2,
		default = AM,
		help_text = _('shift: AM? PM?')
		)

    date = models.DateField(
		help_text = _('date')
		)

    age = models.CharField(
		max_length = 20,
		blank = True,
		null = True,
		help_text = _('age: Adult? Juvenile? leave it blank if do not known')
		)

    primary_fur_color = models.CharField(
		max_length = 20,
		blank = True,
		null = True,
		help_text = _('primary fur color: Gray? Cinnamon? Black? leave it blank if do not known')
		)

    location = models.CharField(
		max_length = 50,
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

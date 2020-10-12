from django.db  import models
  
class Sightings(models.Model):
    latitude = models.DecimalField(
            max_digits = 17,
            decimal_places = 15
            )
			
    longitude = models.DecimalField(
            max_digits = 17,
            decimal_places = 15
            )
			
    unique_squirrel_id = models.CharField(
            max_length = 15,
            )
	
    shift = models.CharField(
            max_length = 2
            )
			
    date = models.CharField(
	    max_length = 8
	    )
			
    age = models.CharField(
            max_length = 15,
            blank = True,
	    null = True
            )
			
    primary_fur_color = models.CharField(
            max_length = 20,
            blank = True,
            null = True
            )
			
    location = models.CharField(
            max_length = 30,
            blank = True,
	    null = True
            )
			
    specifi_location = models.TextField(
            blank = True,
            null = True
            )
			     
    running = models.BooleanField()
	
    chasing = models.BooleanField()
	
    climbing = models.BooleanField()
    
    eating = models.BooleanField()
    
    foraging = models.BooleanField()
    
    other_activities = models.TextField(
            blank = True,
	    null = True
            )
    
    kuks = models.BooleanField()
	
    quaas = models.BooleanField()
        	
    moans = models.BooleanField()
        	
    tail_flags = models.BooleanField()
        	
    tail_twitches = models.BooleanField()
        	
    approaches = models.BooleanField()
        	
    indifferent = models.BooleanField()
        	
    runs_from = models.BooleanField()



# Create your models here.

from django.db  import models
  
class Sightings(models.Model):
    latitude = models.CharField(
            max_length = 20
            )
			
    longitude = models.CharField(
            max_length = 20
            )
			
    unique_squirrel_id = models.CharField(
            max_length = 15
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
			     
    running = models.CharField(max_length = 8)
	
    chasing = models.CharField(max_length = 8)
	
    climbing = models.CharField(max_length = 8)
    
    eating = models.CharField(max_length = 8)
    
    foraging = models.CharField(max_length = 8)
    
    other_activities = models.TextField(
            blank = True,
	    null = True
            )
    
    kuks = models.CharField(max_length = 8)
	
    quaas = models.CharField(max_length = 8)
	
    moans = models.CharField(max_length = 8)
	
    tail_flags = models.CharField(max_length = 8)
	
    tail_twitches = models.CharField(max_length = 8)
    
    approaches = models.CharField(max_length = 8)
	
    indifferent = models.CharField(
            max_length = 8,
            null = True
            )
	
    runs_from = models.CharField(max_length = 8)
			

# Create your models here.

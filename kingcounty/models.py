from tabnanny import verbose
from django.db import models
from geopy.geocoders import Nominatim

# Create your models here.

class Data(models.Model):
    city = models.CharField(max_length=100, null=True)
    county = models.CharField(max_length=500, null=True)
    crime_count = models.PositiveBigIntegerField(null=True)
    crime_count_normalized = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    
    class Meta:
        verbose_name_plural= "Data"
    
    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="Your_Name")
        loc = geolocator.geocode(self.city+','+ self.county)
        self.latitude = loc.latitude
        self.longitude= loc.longitude
        return super().save(*args, **kwargs)
        
    def __str__(self):
        return self.city

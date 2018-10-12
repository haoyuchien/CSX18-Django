from django.db import models
from django.conf import settings

# Create your models here.

class TourDates(models.Model):
    city = models.CharField(max_length=25, blank=False)
    venue = models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.city + " " + self.venue + " " + self.date
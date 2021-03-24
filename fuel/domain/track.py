from django.db import models
from django.conf import settings


class Track(models.Model): 
    name = models.CharField(max_length = 200)
    country = models.CharField(max_length = 200) 
    distance = models.PositiveSmallIntegerField() 
    turns = models.PositiveSmallIntegerField()
    lap_time = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "track"
        verbose_name_plural = "tracks"
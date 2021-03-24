from django.db import models
from django.conf import settings

from .car import Car
from .track import Track

class Consumption(models.Model): 
    car = models.ForeignKey(Car, null=False, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, null=False, on_delete=models.CASCADE)
    fuel = models.FloatField() 

    def __str__(self):
        return f"{ self.car } / { self.track } = {self.fuel}L/lap"

    class Meta:
        verbose_name = "consumption"
        verbose_name_plural = "consumptions"


class CustomConsumption(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, null=False, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, null=False, on_delete=models.CASCADE)
    fuel = models.FloatField() 

    def __str__(self):
        return f"{ self.car } / { self.track } = {self.fuel}L/lap"

    class Meta:
        verbose_name = "custom_consumption"
        verbose_name_plural = "custom_consumptions"
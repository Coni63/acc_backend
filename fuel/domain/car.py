from django.db import models
from django.conf import settings


class Car(models.Model): 
    name = models.CharField(max_length = 200)
    brand = models.CharField(max_length = 200) 

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"
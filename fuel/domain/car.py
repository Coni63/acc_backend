from django.db import models
from django.conf import settings


class Car(models.Model): 
    name = models.CharField(max_length = 200)
    brand = models.CharField(max_length = 200) 
    category = models.CharField(max_length = 5, default="GT3") 

    def __str__(self):
        return f"{self.category} - {self.brand} {self.name}"

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"
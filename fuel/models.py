from django.db import models


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


class Car(models.Model): 
    name = models.CharField(max_length = 200)
    brand = models.CharField(max_length = 200) 

    def __str__(self):
        return f"{self.brand} {self.name}"

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"


class Consumption(models.Model): 
    car = models.ForeignKey(Car, null=False, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, null=False, on_delete=models.CASCADE)
    fuel = models.FloatField() 

    def __str__(self):
        return f"{ self.car } / { self.track } = {self.fuel}L/lap"

    class Meta:
        verbose_name = "consumption"
        verbose_name_plural = "consumptions"
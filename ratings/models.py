from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Ratings(models.Model): 
    player = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    datetime = models.DateTimeField(auto_now=True) 
    total = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(9999)], null=False) 
    TR = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=False)
    CN = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=False)
    CC = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=False)
    PC = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=False)
    SA = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=False)
    RC = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=False)
    CP = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(99)], null=True, default=0)

    def __str__(self):
        return f"{ self.player } - { self.total } pts"

    class Meta:
        verbose_name = "ratings"
        verbose_name_plural = "ratings"
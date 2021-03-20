from django.contrib import admin
from .models import Track, Car, Consumption
# Register your models here.

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "distance", "turns", "lap_time")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "brand")


@admin.register(Consumption)
class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ("track", "car", "fuel")
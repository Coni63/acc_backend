from django.contrib import admin
from .domain.car import Car
from .domain.track import Track
from .domain.consumption import  Consumption, CustomConsumption

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "distance", "turns", "lap_time_gt3", "lap_time_gt4")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "category")


@admin.register(Consumption)
class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ("track", "car", "fuel")


@admin.register(CustomConsumption)
class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ("user", "track", "car", "fuel")
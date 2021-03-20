from django.contrib import admin
from .models import Ratings


@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ratings._meta.fields if field.name != "id"]
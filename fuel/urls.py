from django.urls import path
from django.contrib import admin

from .controllers.car import CarController 
from .controllers.track import TrackController 
from .controllers.consumption import ConsumptionController 

admin.site.site_header = 'Assetto Corsa Competizione'
admin.site.index_title = 'Admin Panel'
admin.site.site_title = 'Admin Panel'

urlpatterns = [
    path('car', CarController.as_view()),
    path('track', TrackController.as_view()),
    path('consumption', ConsumptionController.as_view()),
]

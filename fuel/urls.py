from django.urls import path
from django.contrib import admin

from .views import CarList, ConsumptionList, TrackList

admin.site.site_header = 'Assetto Corsa Competizione'
admin.site.index_title = 'Admin Panel'
admin.site.site_title = 'Admin Panel'

urlpatterns = [
    path('consumption', ConsumptionList.as_view()),
    path('car', CarList.as_view()),
    path('track', TrackList.as_view())
]

from django.urls import path
from django.contrib import admin

from .views import RatingsAPI, AvgRatingsAPI, HistRatingsAPI

admin.site.site_header = 'Assetto Corsa Competizione'
admin.site.index_title = 'Admin Panel'
admin.site.site_title = 'Admin Panel'

urlpatterns = [
    path('me', RatingsAPI.as_view()),
    path('average', AvgRatingsAPI.as_view()),
    path('distribution', HistRatingsAPI.as_view()),
]

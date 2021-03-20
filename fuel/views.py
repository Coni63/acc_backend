from django.shortcuts import render

from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView


from .models import Car, Consumption, Track
from .serializers import CarSerializer, ConsumptionSerializer, TrackSerializer


class ConsumptionList(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ConsumptionSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Consumption.objects.all()
        car = self.request.query_params.get('car', None)
        if car is not None:
            queryset = queryset.filter(car=car)
        track = self.request.query_params.get('track', None)
        if track is not None:
            queryset = queryset.filter(track=track)

        return queryset


class CarList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class TrackList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
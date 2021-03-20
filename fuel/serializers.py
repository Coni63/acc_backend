from rest_framework import serializers

from .models import Car, Track, Consumption

class ConsumptionSerializer(serializers.Serializer):
    track = serializers.CharField(max_length=200)
    car = serializers.CharField(max_length=200)
    fuel = serializers.FloatField()

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'name', 'brand')


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'name', 'country', 'distance', 'turns', 'lap_time')

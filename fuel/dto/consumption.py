from rest_framework import serializers

from ..domain.consumption import Consumption, CustomConsumption


class CustomConsumptionSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CustomConsumption
        fields = ('user', 'track', 'car', 'fuel')


class ConsumptionSerializer(serializers.Serializer):
    track = serializers.CharField(max_length=200)
    car = serializers.CharField(max_length=200)
    fuel = serializers.FloatField()

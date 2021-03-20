from rest_framework import serializers
from .models import Ratings

class RatingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ratings
        fields = "__all__"
        read_only_fields = ('player', 'datetime')

    def create(self, validated_data, user):
        return Ratings.objects.create(**validated_data, player=user)
from rest_framework import serializers

from ..domain.track import Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'name', 'country', 'distance', 'turns', 'lap_time_gt3', 'lap_time_gt4')

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from ..application.track import get_tracks_list
from ..dto.track import TrackSerializer


class TrackController(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        Return a list of all track.
        """
        tracks = get_tracks_list()
        serializer = TrackSerializer(tracks, many=True)
        return Response(serializer.data)
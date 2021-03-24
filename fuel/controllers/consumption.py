from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..application.consumption import get_consumption, save_consumption
from ..dto.consumption import ConsumptionSerializer, CustomConsumptionSerializer


class ConsumptionController(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        Return a list of all track.
        """
        car = request.query_params.get('car', None)
        if car is None:
            return Response({"error": "car not provided"}, status=status.HTTP_400_BAD_REQUEST)

        track = self.request.query_params.get('track', None)
        if track is None:
            return Response({"error": "track not provided"}, status=status.HTTP_400_BAD_REQUEST)

        consumptions = get_consumption(car=car, track=track, user=request.user.id)
        if len(consumptions) == 0:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ConsumptionSerializer(consumptions[0], many=False)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.user.id is None:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        data = request.data
        data["user"] = request.user.id  # embed the user on backend (will overwrite something pushed) -- not able to have it working with hiddenFields

        serializer = CustomConsumptionSerializer(data=data, many=False)
        if serializer.is_valid():
            consumption = save_consumption(**serializer.validated_data)
            serializer = ConsumptionSerializer(consumption, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
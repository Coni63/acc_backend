from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from ..application.car import get_cars_list
from ..dto.car import CarSerializer


class CarController(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        Return a list of all car.
        """
        cars = get_cars_list()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
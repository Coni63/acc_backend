from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib.auth import get_user
from django.db.models import Avg, Max, Min, Func, Count
from rest_framework.permissions import IsAuthenticated
from django_pivot.pivot import pivot
from django_pivot.histogram import histogram

from .models import Ratings
from .serializers import RatingsSerializer

class Round(Func):
  function = 'ROUND'
  arity = 2


class RatingsAPI(APIView):
    serializer_class = RatingsSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = RatingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        snippets = Ratings.objects.filter(player=request.user).order_by('-id')[:10]
        serializer = RatingsSerializer(snippets, many=True)
        return Response(serializer.data)


class AvgRatingsAPI(APIView):
    serializer_class = RatingsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        metrics =  {
            "total" : Round(Avg('total'), 0),
            "TR" : Round(Avg('TR'), 2),
            "CN" : Round(Avg('CN'), 2),
            "CC" : Round(Avg('CC'), 2),
            "PC" : Round(Avg('PC'), 2),
            "SA" : Round(Avg('SA'), 2),
            "RC" : Round(Avg('RC'), 2),
            "CP" : Round(Avg('CP'), 2),
        }

        last_record_per_user = Ratings.objects.values('player').annotate(id= Max("id")).values_list('id', flat=True)  # take the last record per user
        stats = Ratings.objects.filter(id__in = last_record_per_user).aggregate(**metrics)  # compute the average over user
        return Response(dict(stats))


class HistRatingsAPI(APIView):
    serializer_class = RatingsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        last_record_per_user = Ratings.objects.values('player').annotate(id= Max("id")).values_list('id', flat=True)
        subrecord = Ratings.objects.filter(id__in = last_record_per_user)
        ans = {
            "total" : histogram(subrecord, "total", bins=list(range(0, 10000, 250))),
            "TR" : histogram(subrecord, "TR", bins=list(range(0, 100, 5))),
            "CN" : histogram(subrecord, "CN", bins=list(range(0, 100, 5))),
            "CC" : histogram(subrecord, "CC", bins=list(range(0, 100, 5))),
            "PC" : histogram(subrecord, "PC", bins=list(range(0, 100, 5))),
            "SA" : histogram(subrecord, "SA", bins=list(range(0, 100, 5))),
            "RC" : histogram(subrecord, "RC", bins=list(range(0, 100, 5))),
            "CP" : histogram(subrecord, "CP", bins=list(range(0, 100, 5))),
        }
        return Response(ans)
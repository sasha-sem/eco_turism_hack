from django.shortcuts import render
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from api.models import Achievements
from rest_framework.response import Response
from .serializers import AchievementsSerializer
from django.db import connection
from django.http import Http404, HttpResponse
# Create your views here.

class AchievementsList(generics.ListCreateAPIView):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer       
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']


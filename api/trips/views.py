from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from api.models import Trips
from rest_framework.response import Response
from api.trips.serializers import TripsSerializer
from django.db import connection
from django.http import Http404, HttpResponse
# Create your views here.

class TripView(generics.ListCreateAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer       
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['route','reserve','id']

class TripDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer       
    filter_backends = [DjangoFilterBackend]
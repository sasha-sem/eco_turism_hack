from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from api.models import Sights
from rest_framework.response import Response
from .serializers import SightsDetailSerializer,SightsListSerializer
from django.db import connection
from django.http import Http404, HttpResponse
# Create your views here.

class SightsList(generics.ListCreateAPIView):
    queryset = Sights.objects.all()
    serializer_class = SightsListSerializer       
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category_id', 'persons','country_id']

class SightsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sights.objects.all()
    serializer_class = SightsDetailSerializer

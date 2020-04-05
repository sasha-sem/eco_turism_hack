from django.shortcuts import render
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from api.models import Reserves
from rest_framework.response import Response
from .serializers import ReservesDetailSerializer,ReservesListSerializer
from django.db import connection
from django.http import Http404, HttpResponse
# Create your views here.

class ReservesList(generics.ListCreateAPIView):
    queryset = Reserves.objects.all()
    serializer_class = ReservesListSerializer       
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category_id', 'persons','country_id']

class ReservesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserves.objects.all().prefetch_related('pictures')
    serializer_class = ReservesDetailSerializer


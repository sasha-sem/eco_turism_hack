from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from api.models import Routes
from rest_framework.response import Response
from .serializers import RoutesDetailSerializer,RoutesListSerializer
from django.db import connection
from django.http import Http404, HttpResponse
# Create your views here.

class RoutesList(generics.ListCreateAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesListSerializer       
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['reserve']

class RoutesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesDetailSerializer

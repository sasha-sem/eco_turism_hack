from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from api.models import ReserveReview,RouteReview
from rest_framework.response import Response
from  api.reviews.serializers import ReserveReviewSerializer,RouteReviewSerializer
from django.db import connection
from django.http import Http404, HttpResponse
# Create your views here.

class RouteReviewList(generics.ListCreateAPIView):
    queryset = RouteReview.objects.all()
    serializer_class = RouteReviewSerializer       
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['route']

class ReserveReviewList(generics.ListCreateAPIView):
    queryset = ReserveReview.objects.all()
    serializer_class = ReserveReviewSerializer       
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['reserve']
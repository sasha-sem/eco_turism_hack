from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.trips.views import TripView, TripDetailView

urlpatterns = [
    path('trips/', TripView.as_view()),
    path('trips/id/<int:pk>/', TripDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

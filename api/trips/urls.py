from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.trips.views import TripView

urlpatterns = [
    path('trips/', TripView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

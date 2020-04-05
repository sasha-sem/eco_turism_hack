from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SightsDetail, SightsList, SightsDetailList

urlpatterns = [
    path('sights/', SightsList.as_view()),
    path('sights-detailed/', SightsDetailList.as_view()),
    path('sights/id/<int:pk>/', SightsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

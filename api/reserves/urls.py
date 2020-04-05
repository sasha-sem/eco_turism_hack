from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ReservesList,ReservesDetail

urlpatterns = [
    path('reserves/', ReservesList.as_view()),
    path('reserves/id/<int:pk>/', ReservesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

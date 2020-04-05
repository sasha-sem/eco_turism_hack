from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import RoutesDetail,RoutesList

urlpatterns = [
    path('routes/', RoutesList.as_view()),
    path('routes/id/<int:pk>/', RoutesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

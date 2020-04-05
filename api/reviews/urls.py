from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.reviews.views import ReserveReviewList,RouteReviewList

urlpatterns = [
    path('reserves-reviews/', ReserveReviewList.as_view()),
    path('routes-reviews/', RouteReviewList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

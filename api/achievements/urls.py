from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AchievementsList

urlpatterns = [

    path("achievements/",AchievementsList.as_view(),name="achievements"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

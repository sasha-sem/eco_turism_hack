from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileListCreateView, userProfileDetailView,userProfile_list 

urlpatterns = [
    #gets all user profiles and create a new profile
    path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
    path("profiles",userProfile_list,name="profiles"),
   # retrieves profile details of the currently logged in user
    path("profile/id/<int:pk>",userProfileDetailView.as_view(),name="profile"),
]

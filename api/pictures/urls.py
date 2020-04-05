from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PictureDetailView, picture_list, success, upload_file

urlpatterns = [
    path("pictures/id/<int:pk>",PictureDetailView.as_view(),name="picture"),
    path("pictures/",picture_list,name="pictures"),
    path('upload_file', upload_file, name = 'image_upload'), 
    path('success', success, name = 'success'), 
]

urlpatterns = format_suffix_patterns(urlpatterns)

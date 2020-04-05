from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from api.models import ReviewsPictures
from rest_framework.response import Response
from  api.pictures.serializers import PicturesSerializer,PicturesListSerializer
from django.db import connection
from django.shortcuts import render, redirect 
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from .forms import PictureForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return JsonResponse({'success':True,'id':form.instance.id}) 
    else:
        form = PictureForm()
    return JsonResponse({'success':False}) 

def success(request): 
    return HttpResponse('successfully uploaded') 
@api_view(['GET'])
def picture_list(request):
    if request.method == 'GET':
        snippets = ReviewsPictures.objects.all()
        serializer = PicturesListSerializer(snippets, many=True)
        return Response(serializer.data)

class PictureDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewsPictures.objects.all()
    serializer_class = PicturesSerializer


from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated,AllowAny
from api.models import userProfile
from django_filters.rest_framework import DjangoFilterBackend
from api.accounts.permissions import IsOwnerProfileOrReadOnly
from api.accounts.serializers import userProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def userProfile_list(request):
    if request.method == 'GET':
        kwargs = request.query_params
        snippets = userProfile.objects.get(id=kwargs['id'])
        serializer = userProfileSerializer(snippets, many=False)
        return Response(serializer.data)
        
class UserProfileListCreateView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['known_routes','is_guide']
    serializer_class=userProfileSerializer
    permission_classes=[AllowAny]
    #def get_queryset(self):
    #    id_list = self.request.GET.getlist("route")
    #    if not id_list:
    #        return []
    #    return userProfile.objects.filter(id__in=id_list)
    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)
        
class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]
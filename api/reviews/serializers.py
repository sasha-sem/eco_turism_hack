from rest_framework import serializers
from api.models import  RouteReview,ReserveReview

class RouteReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=RouteReview
        fields='__all__'
class ReserveReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReserveReview
        fields='__all__'

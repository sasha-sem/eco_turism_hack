from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from api.models import Routes, RouteReview
from django.db.models import Sum

class RoutesListSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Routes
        geo_field = "geom"
        fields = ('id', 'name',)
class RoutesDetailSerializer(GeoFeatureModelSerializer):
    rating = serializers.SerializerMethodField()
    def get_rating(self, instance):
        rate_sum = RouteReview.objects.filter(route=instance.id).aggregate(sum=Sum('rating'))['sum']
        print(rate_sum)
        rate_count = RouteReview.objects.filter(route=instance.id).count()
        print(rate_count)
        rate = 0
        if rate_count!=0:
            rate = rate_sum / rate_count
        return rate
    class Meta:
        model = Routes
        geo_field = "geom"
        fields = '__all__'

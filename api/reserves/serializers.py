from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from api.models import Reserves, ReserveReview,ReviewsPictures
from api.pictures.serializers import PicturesSerializer
from django.db.models import Sum

class ReservesListSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Reserves
        geo_field = "geom"
        fields = ('id', 'name',)
class ReservesDetailSerializer(GeoFeatureModelSerializer):
    pictures=PicturesSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()
    def get_rating(self, instance):
        rate_sum = ReserveReview.objects.filter(reserve=instance.id).aggregate(sum=Sum('rating'))['sum']
        rate_count = ReserveReview.objects.filter(reserve=instance.id).count()
        rate = 0
        if rate_count!=0:
            rate = rate_sum / rate_count
        return rate
    class Meta:
        model = Reserves
        geo_field = "geom"
        fields = ('id', 'name', 'descr', 'pictures','rating')


from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from api.models import Sights

class SightsListSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Sights
        geo_field = "geom"
        fields = ('id', 'name',)
class SightsDetailSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Sights
        geo_field = "geom"
        fields = '__all__'

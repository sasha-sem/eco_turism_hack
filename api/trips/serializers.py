from rest_framework import serializers
from api.models import  Trips

class TripsSerializer(serializers.ModelSerializer):
    #reserve = serializers.SerializerMethodField()
    #def get_reserve(self, obj):
    #    return obj.route.reserve.id
    class Meta:
        model=Trips
        fields='__all__'

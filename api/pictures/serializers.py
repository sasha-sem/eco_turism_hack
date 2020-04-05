from rest_framework import serializers
from api.models import ReviewsPictures

class PicturesSerializer(serializers.ModelSerializer):
      picture_url = serializers.SerializerMethodField()

      class Meta:
            model = ReviewsPictures
            fields = ('id','picture_url') 

      def get_picture_url(self, obj):
            request = self.context.get('request')
            if obj.picture and hasattr(obj.picture, 'url'):
               picture_url = obj.picture.url
               return request.build_absolute_uri(picture_url)
            else:
               return None
class PicturesListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReviewsPictures
        fields='__all__'
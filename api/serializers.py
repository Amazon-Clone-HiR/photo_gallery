from rest_framework import serializers
from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
  class Meta():
    model = Photo
    fields = ('id', 'created_at', 'photo_name', 'item_name', 'src', 'item_id')
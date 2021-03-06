from rest_framework import generics

from .models import Photo
from .serializers import PhotoSerializer

# Create your views here.
class PhotoListByItem(generics.ListAPIView):
  serializer_class = PhotoSerializer
  
  def get_queryset(self):
    if 'item_id' in self.kwargs:
      item_id = self.kwargs['item_id']
      return Photo.objects.filter(item_id=item_id)
    item_name = self.kwargs['item_name']
    return Photo.objects.filter(item_name=item_name)

# class PhotoListByItemName(generics.ListAPIView):
#   serializer_class = PhotoSerializer

#   def get_queryset(self):
#     item_name = self.kwargs['item_name']
#     return Photo.objects.filter(item_name=item_name)

# class PhotoDetail(generics.RetrieveAPIView):
#   queryset = Photo.objects.all()
#   serializer_class = PhotoSerializer
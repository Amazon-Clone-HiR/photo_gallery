from rest_framework import generics

from .models import Photo
from .serializers import PhotoSerializer

# Create your views here.
class PhotoList(generics.ListCreateAPIView):
  serializer_class = PhotoSerializer
  
  def get_queryset(self):
    item_id = self.kwargs['item_id']
    return Photo.objects.filter(item_id=item_id)

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Photo.objects.all()
  serializer_class = PhotoSerializer
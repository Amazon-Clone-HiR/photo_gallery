from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Photo
from .serializers import PhotoSerializer

# Create your views here.
@csrf_exempt
def photo_list(request):
  if request.method == 'GET':
    photos = Photo.objects.all()
    serializer = PhotoSerializer(photos, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = PhotoSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def photo_detail(request, pk):
  try:
    photo = Photo.objects.get(pk=pk)
  except Photo.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = PhotoSerializer(photo)
    return JsonResponse(serializer.data)
  
  elif request.method == 'PUT':
    data = JSON.parser().parse(request)
    serializer = PhotoSerializer(photo, data=data)
    if serializer.is_valid():
      serializer.save()
      return JsonResponse(serializer.data)
    return JsonResponse(status=400)
  
  elif request.method == 'DELETE':
    photo.delete()
    return JsonResponse(status=204)


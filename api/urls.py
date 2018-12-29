from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
  path('api/photos/', views.PhotoList.as_view(), name="photo_list"),
  path('api/photos/<int:pk>/', views.PhotoDetail.as_view(), name="photo_detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)
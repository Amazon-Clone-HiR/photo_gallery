from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
  path('api/photos/<int:item_id>/', views.PhotoList.as_view(), name="photo_list_by_item_id"),
  path('api/photos/photo/<int:pk>/', views.PhotoDetail.as_view(), name="photo_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
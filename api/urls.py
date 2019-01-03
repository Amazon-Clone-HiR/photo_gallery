from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
  path('items/<uuid:item_id>/', views.PhotoListByItem.as_view(), name="photo_list_by_item_id"),
  path('items/<str:item_name>/', views.PhotoListByItem.as_view(), name="photo_list_by_item_name"),
  # path('photos/photo/<int:pk>/', views.PhotoDetail.as_view(), name="photo_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
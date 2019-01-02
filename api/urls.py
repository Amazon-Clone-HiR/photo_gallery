from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
  path('items/<int:item_id>/', views.PhotoListByItemID.as_view(), name="photo_list_by_item_id"),
  path('items/<str:item_name>/', views.PhotoListByItemName.as_view(), name="photo_list_by_item_name"),
  path('photos/photo/<int:pk>/', views.PhotoDetail.as_view(), name="photo_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
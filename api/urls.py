from django.urls import path
from api import views

urlpatterns = [
  path('api/photos/', views.photo_list, name="photo_list"),
  path('api/photos/<int:pk>/', views.photo_detail, name="photo_detail")
]
from django.db import models
import random

# Create your models here.
class Photo(models.Model):
  created_at = models.DateTimeField(auto_now=True)
  photo_name = models.CharField(max_length=200)
  src = models.CharField(max_length=200)
  item_id = models.IntegerField(default=random.randint(1,50))
  item_name = models.CharField(max_length=200)
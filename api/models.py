from django.db import models
import random
import uuid

# Create your models here.
class Photo(models.Model):
  created_at = models.DateTimeField(auto_now=True)
  photo_name = models.CharField(max_length=200)
  src = models.CharField(max_length=200)
  item_id = models.UUIDField(default=uuid.uuid4)
  item_name = models.CharField(max_length=200)
  is_primary = models.BooleanField(default=False)
from django.db import models

# Create your models here.
class Photo(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=200)
  src = models.CharField(max_length=200)
  item_id = models.IntegerField(default=1)

  class Meta:
    ordering = ('created_at',)
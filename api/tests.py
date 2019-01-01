from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Photo

# Create your tests here.
class PhotoTestCase(APITestCase):
  def setUp(self):
    # post to test db so we can test GETs

  def test_get_photos_by_item_id(self):
    """
    Ensure we can retrieve all pictures by the associated item_id
    """
    response = self.client.get('/api/items/4/photos/')
    print(response.content)


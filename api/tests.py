from django.test import TestCase
from .models import Photo

# Create your tests here.
class PhotoTestCase(TestCase):
  def setUp(self):
    Photo.objects.create(name="cat pic", src="kitty.jpg")
    Photo.objects.create(name="cat pic 2.0", src="bigkitty.jpg")
  
  def test_assert_photos_are_created(self):
    first = Photo.objects.get(name="cat pic")
    second = Photo.objects.get(name="cat pic 2.0")
    self.assertEqual(first.src, "kitty.jpg")
    self.assertEqual(second.src, "bigkitty.jpg")

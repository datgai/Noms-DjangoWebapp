from django.test import SimpleTestCase
from django.urls import reverse, resolve
from foodie.views import CustomLoginView, RegisterView, index, bmi, calories 

class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEqual(resolve(url).func, index)
    
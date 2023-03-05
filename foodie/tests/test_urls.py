from django.test import SimpleTestCase
from django.urls import reverse, resolve
from foodie.views import CustomLoginView, RegisterView, index, bmi, calories 
from django.contrib.auth import views as auth_views

class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)
    
    def test_bmi_url_is_resolved(self):
        url = reverse('bmi')
        self.assertEqual(resolve(url).func, bmi)

    def test_calories_url_is_resolved(self):
        url = reverse('calories')
        self.assertEqual(resolve(url).func,calories)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class, CustomLoginView)
    
    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, RegisterView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)
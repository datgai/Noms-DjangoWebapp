from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import models
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.bmi_url = reverse('bmi')
        self.calories_url = reverse("calories")
        self.login_url = reverse("login")
        self.logout_url = reverse("logout")
        self.register_url = reverse("register")

    def test_foodie_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'foodie/index.html')

    def test_foodie_bmi_GET(self):
        response = self.client.get(self.bmi_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'foodie/bmi.html')
    
    def test_foodie_calories_GET(self):
        response = self.client.get(self.calories_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'foodie/calories.html')

    def test_foodie_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'foodie/login.html')
    
    def test_foodie_logout_GET(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'foodie/logout.html')
    
    def test_foodie_calories_GET(self):
        response = self.client.get(self.calories_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'foodie/calories.html')
    
    def test_foodie_register_POST_add_new_account(self):
        response = self.client.post(self.register_url, {
            'first_name': 'test',
            'last_name': 'user',
            'username':'TESTER',
            'email':'test@mail.com',
            'password1':'DONKEYkong12#',
            'password2':'DONKEYkong12#'
        })
        
        self.assertEquals(response.status_code, 200)
        user = (list(models.User.objects.values('first_name','last_name','username','email','is_staff','is_superuser')))[0]
        self.assertEqual(user['first_name'],'test')
        self.assertEqual(user['last_name'],'user')
        self.assertEqual(user['username'],'TESTER')
        self.assertEqual(user['email'],'test@mail.com')
        self.assertFalse(user['is_staff'])
        self.assertFalse(user['is_superuser'])
        
    def test_foodie_login_POST_login_account(self):
         self.test_foodie_register_POST_add_new_account()
         response = self.client.post(self.login_url, {
            'username':'TESTER',
            'password':'DONKEYkong12#',
        })
         self.assertEqual(response.wsgi_request.user.get_username(),'TESTER')

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Food_model

# Create your tests here.
class Food_model_Test(TestCase):
    def setUp(self):
        User.objects.create(username="testUser")
        Food_model.objects.create(food_name="grass", food_calories= 33, food_protein= 2.2, food_fat = 0)
    
    def test_food_exists(self):
        grass = Food_model.objects.get(food_name="grass")
from django.test import TestCase
from .forms import NomForm
from django.contrib.auth.models import User
from .models import Food_model

class TestForms(TestCase):
    def test_valid_data(self):
        form = NomForm(data={
            'food_name':'testfood',
            'food_time':'12:05:03',
            'food_date':'2020-12-01',
            'food_calories':0,
            'food_protein':0,
            'food_fat':0,
            'food_saturatedfat':0,
            'food_sodium':0,
            'food_potassium':0,
            'food_carb':0,
            'food_fiber':0
        })
        self.assertTrue(form.is_valid())
        User.objects.create(username="testUser")
        form.save()
        self.assertEqual(list(Food_model.objects.values())[0]['food_name'],'testfood')
    
    def test_invalid_time(self):
        form = NomForm(data={
            'food_name':'testfood',
            'food_time':'13:65:03',
            'food_date':'2020-12-01',
            'food_calories':0,
            'food_protein':0,
            'food_fat':0,
            'food_saturatedfat':0,
            'food_sodium':0,
            'food_potassium':0,
            'food_carb':0,
            'food_fiber':0
        })
        self.assertFalse(form.is_valid())

    def test_invalid_date(self):
        form = NomForm(data={
            'food_name':'testfood',
            'food_time':'13:05:03',
            'food_date':'2020-13-01',
            'food_calories':0,
            'food_protein':0,
            'food_fat':0,
            'food_saturatedfat':0,
            'food_sodium':0,
            'food_potassium':0,
            'food_carb':0,
            'food_fiber':0
        })
        self.assertFalse(form.is_valid())
    
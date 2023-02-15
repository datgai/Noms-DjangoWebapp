from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Food_model(models.Model):
    food_name = models.CharField(max_length=100,verbose_name="Meal Name")
    food_time = models.TimeField('Time of meal:',default=timezone.now)
    food_date = models.DateField('Date of meal:',default=timezone.now)
    food_calories = models.IntegerField(default=0,help_text="cal",verbose_name='Calories')
    food_protein = models.IntegerField(default=0,help_text="g",verbose_name='Protein')
    food_fat = models.IntegerField(default=0,help_text="g",verbose_name='Total Fat')
    food_saturatedfat=models.IntegerField(default=0,help_text="g",verbose_name='Saturated Fat')
    food_sodium = models.IntegerField(default=0,help_text="mg",verbose_name='Sodium')
    food_potassium = models.IntegerField(default=0,help_text="mg",verbose_name='Potassium')
    food_carb = models.IntegerField(default=0,help_text="g",verbose_name='Total Carbohydrate')
    food_fiber = models.IntegerField(default=0,help_text="g",verbose_name='Dietary Fiber')
    food_eater = models.ForeignKey(User, on_delete=models.CASCADE, default="1")

    def __str__(self):
        return self.food_name

    def is_today(self):
        return self.food_date >= timezone.now() - datetime.timedelta(days=1)
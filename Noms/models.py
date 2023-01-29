from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Food_model(models.Model):
    food_name = models.CharField(max_length=100)
    food_date = models.DateField('Date eaten:')
    food_time = models.TimeField('Time eaten:')
    food_calories = models.IntegerField(default=0)
    food_protein = models.IntegerField(default=0)
    food_fat = models.IntegerField(default=0)
    food_saturatedfat=models.IntegerField(default=0)
    food_sodium = models.IntegerField(default=0)
    food_carb = models.IntegerField(default=0)
    food_fiber = models.IntegerField(default=0)
    #food_eater

    def __str__(self):
        return self.food_name

    def is_today(self):
        return self.food_date >= timezone.now() - datetime.timedelta(days=1)
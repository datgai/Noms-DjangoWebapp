from django import forms

class NomForm(forms.Form):
    food_name = forms.CharField(label='Food Name',max_length=100)
    food_date = forms.DateField()
    food_time = forms.TimeField()
    food_calories = forms.IntegerField()
    food_protein = forms.IntegerField()
    food_fat = forms.IntegerField()
    food_saturatedfat=forms.IntegerField()
    food_sodium = forms.IntegerField()
    food_carb = forms.IntegerField()
    food_fiber = forms.IntegerField()
    
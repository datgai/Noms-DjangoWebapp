from django import forms
from .models import Food_model
import datetime

class NomForm(forms.ModelForm):
    class Meta:
        model = Food_model
        fields = ('food_name','food_date','food_calories','food_protein','food_fat','food_saturatedfat','food_sodium','food_potassium','food_carb','food_fiber')

        widgets = {'food_name' : forms.TextInput(attrs={'class' : 'inputform'}),
        'food_date' : forms.DateInput(attrs={'class' : 'inputform','value': datetime.datetime.now().strftime("%d-%m-%Y")}),
        'food_time' : forms.TimeInput(attrs={'class' : 'inputform'}),
        'food_calories' : forms.NumberInput(attrs={'class' : 'inputform'}),
        'food_protein' : forms.NumberInput(attrs={'class' : 'inputform'}),
        'food_fat' : forms.NumberInput(attrs={'class' : 'inputform'}),
        'food_saturatedfat' : forms.NumberInput(attrs={'class' : 'inputform'}),
        'food_sodium' : forms.NumberInput(attrs={'class' : 'inputform'}),
        'food_potassium' : forms.NumberInput(attrs={'class' : 'inputform'}),
        'food_carb' : forms.NumberInput(attrs={'class' : 'inputform'}),
        'food_fiber' : forms.NumberInput(attrs={'class' : 'inputform'})}
    
    
from django.shortcuts import render, get_object_or_404,redirect

from .forms import NomForm

from .models import Food_model

# Create your views here.

def history(request):
    food_list = Food_model.objects.filter(food_eater = request.user.id)
    return render(request, "Noms/history.html",{'food_list':food_list})

def nom(request):
    if request.method == 'POST':
        foodform = NomForm(request.POST)
        if foodform.is_valid():
            foodform.save()
            return redirect("index")
    else:
        foodform = NomForm
    
    return render(request, "Noms/nom.html", {'form': foodform})

def detail(request,nom_id):
    food = get_object_or_404(Food_model, pk=nom_id)
    return render(request, "Noms/detail.html",{'food':food})

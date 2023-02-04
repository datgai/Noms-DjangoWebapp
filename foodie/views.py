from django.shortcuts import render,HttpResponse
from .forms import LoginForm, RegisterForm

# Create your views here.
def index(request):
    return render(request, "foodie/index.html")

def login(request):
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            return render(request, "foodie/index.html")
    else:
        loginform = LoginForm
    
    return render(request, "foodie/login.html", {'form': loginform})

def register(request):
    if request.method == 'POST':
       registerform = RegisterForm(request.POST)
       if registerform.is_valid():
            return render(request, "foodie/index.html")
    else:
        registerform = RegisterForm
    
    return render(request, "foodie/register.html", {'form': registerform})

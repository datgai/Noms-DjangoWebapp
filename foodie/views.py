from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import LoginForm, RegisterForm

# Create your views here.
def index(request):
    return render(request, "foodie/index.html")

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'foodie/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return render(request,'foodie/index.html')

        return render(request, self.template_name, {'form': form})
    
def bmi(request):
    if request.method == 'POST':
        pass
    return render(request,'foodie/bmi.html')

def calories(request):
    if request.method == 'POST':
        pass
    return render(request,'foodie/calories.html')
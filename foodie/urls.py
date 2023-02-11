from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from .views import RegisterView, CustomLoginView
from .forms import LoginForm

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='foodie/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='foodie/logout.html'), name='logout'),
    path("register/", RegisterView.as_view(),name='register')
]
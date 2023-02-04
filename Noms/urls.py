from django.urls import path

from . import views

app_name = 'noms'
urlpatterns = [
    path('', views.index, name='index'),
    path('nom', views.nom, name='nom'),
    path('<int:nom_id>/', views.history, name='history'),
]
from django.urls import path

from . import views

app_name = 'noms'
urlpatterns = [
    path('', views.history , name='history'),
    path('nom', views.nom, name='nom'),
    path('<int:nom_id>/', views.detail,name='detail'),
]
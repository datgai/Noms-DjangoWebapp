from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('nom', views.nom, name='nom'),
    path('<int:nom_id>/', views.detail, name='detail'),
]
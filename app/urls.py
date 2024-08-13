# app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Ajoutez ici d'autres chemins d'URL
]

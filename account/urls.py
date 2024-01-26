from django.urls import path
from .views import profil

urlpatterns = [
    path('profil/', profil, name='profil'),
]

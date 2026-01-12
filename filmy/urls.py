from django.urls import path
from .views import filmy, ulubione

urlpatterns = [
    path("", filmy, name="filmy"),
    path('ulubione/', ulubione, name='ulubione'),
]

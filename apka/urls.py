from django.urls import path
from .views import filmy, ulubione, test

urlpatterns = [
    path("", filmy, name="filmy"),
]
    

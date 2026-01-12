from django.urls import path
from .views import filmy, ulubione, test

urlpatterns = [
    path("", filmy, name="filmy"),
    path('ulubione/', ulubione, name='ulubione'),
    path("test/",test, name='test')
]

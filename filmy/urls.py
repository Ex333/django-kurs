from django.urls import path
from .views import filmy

urlpatterns = [
    path("", filmy, name="filmy"),
]

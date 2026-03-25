from django.urls import path
from .views import home, kontakt, dziekuje 

urlpatterns = [
    path("", home ,name="home"),
    path("kontakt/",kontakt, name ="kontakt"),
    path("dziekuje/", dziekuje ,name="dziekuje")
]
    

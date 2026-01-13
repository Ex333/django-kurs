from django.db import models

class Film(models.Model):
    tytuł =models.CharField(max_length=64)
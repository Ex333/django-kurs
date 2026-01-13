from django.db import models

class Film(models.Model):

    class Kategoria(models.TextChoices):
        AKCJA = "akcja", "Akcja"
        KOMEDIA = "komedia", "Komedia"
        DRAMAT = "dramat", "Dramat"
        HORROR = "horror", "Horror"
        SCI_FI = "sci-fi", "Sci-Fi"
        FANTASY = "fantasy", "Fantasy"
        ANIMACJA = "animacja", "Animacja"
        DOKUMENTALNY = "dokumentalny", "Dokumentalny"

    tytul = models.CharField(max_length=64, unique=True)
    opis = models.TextField(blank=True)
    rok_produkcji = models.PositiveSmallIntegerField(null=True, blank=True)
    kategoria = models.CharField(max_length=32, choices=Kategoria.choices)
    zdjecie = models.ImageField(upload_to="filmy/", null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    def __str__(self):
        return self.tytul + str(self.rok_produkcji)
    
    class Meta:
        ordering = ['tytul']

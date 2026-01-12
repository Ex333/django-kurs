from django.db import models

# Create your models here.
class Film(models.Model):
    tytul = models.CharField(max_length=100,blank=False, unique=True)
    rok = models.IntegerField(blank=False)
    opis = models.TextField(blank=True)
    premiera = models.DateField(blank=True, null=True)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    plakat = models.ImageField(upload_to='plakaty/', blank=True, null=True)

    def __str__(self):
        return f"{self.tytul} ({self.rok})"
    
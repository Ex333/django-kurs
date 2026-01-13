from django.contrib import admin
from .models import Film

#admin.site.register(Film) You can register the model like this or better like below:
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("id", "tytul", "rok_produkcji", "kategoria")
    search_fields = ("tytul", "kategoria", "rok_produkcji")
    list_filter = ("kategoria", "rok_produkcji")
from django.shortcuts import render
from django.http import HttpResponse

def filmy(request):
    return render(request, "filmy.html")

def ulubione(request):
    return render(request, "ulubione.html")

def test(request):
    text = ["czekolada", "banan", "truskawka", "wanilia"]
    return render(request, "test.html", {'text': text})

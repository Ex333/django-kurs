from django.shortcuts import render

def filmy(request):
    return render(request, "filmy.html")

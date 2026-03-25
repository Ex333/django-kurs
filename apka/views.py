from django.shortcuts import render, redirect
from .forms import ContactForm


def kontakt(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        text = form.cleaned_data["text"]

        print(name, email, text)  

        return redirect("dziekuje")

    return render(request, "kontakt.html", {"form": form})

def dziekuje(request):
    return render(request, "dziekuje.html")


def home(request):
    return render(request, "home.html")
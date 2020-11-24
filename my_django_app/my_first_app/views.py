from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "my_first_app/index.html")


def greet(request, name):
    return render(request, "my_first_app/greet.html", {
        # context is where variables have access to
        "name": name.capitalize()
    })

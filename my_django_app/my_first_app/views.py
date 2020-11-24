from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):
    return render(request, "my_first_app/index.html")


def greet(request, name):
    return render(request, "my_first_app/greet.html", {
        # context is where variables have access to
        "name": name.capitalize()
    })


# Create your views here.
def newyear(request):
    now = datetime.datetime.now()
    return render(request, "my_first_app/newyear.html", {
        "newyear": now.month == 1 and now.day == 1,
    })

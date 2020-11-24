from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # str:name is input from url, passes to greet1 function which takes as input: name
    path("<str:name>", views.greet, name="greet"),

]

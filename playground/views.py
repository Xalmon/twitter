from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def welcome(request):
    return HttpResponse("Welcome to Django")


def hello_user(request, name):
    return render(request, 'hello.html', {"name": name})


def one_user(request, one):
    return render(request, 'one.html', {"one": one})

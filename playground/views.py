from django.shortcuts import render
from django.http import HttpResponse

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = '2525'
DEFAULT_FROM_EMAIL = 'complaints@twitter.com'
from django.core.mail import send_mail, send_mass_mail, BadHeaderError


# Create your views here.


def welcome(request):
    return HttpResponse("Welcome to Django")


def hello_user(request, name):
    try:
        message = "hello {name}, stop passing rubbish"
        send_mail("warning", message, 'complaints@tweeta.com', ['xalmonoyefule@gmail.com'])
    except BadHeaderError:
        pass
    return render(request, 'hello.html', {"name": name})


def one_user(request, one):
    return render(request, 'one.html', {"one": one})

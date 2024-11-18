from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse("<h1>Vista Home!</h1>")
    return render(request, 'home.html', {})


'''def contactenos(request):
    return HttpResponse("<h1>Vista Contacto!</h1>")'''


def contacto(request):
    return render(request, 'contacto.html', {})

from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def vistadmin(request):
    return render(request, 'core/vistadmin.html')

def login(request):
    return render(request, 'core/login.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def vistaresidente(request):
    return render(request, 'vistaresidente.html')

def contacto(request):
    return render(request, 'contacto.html')

def pagogastoscomues(request):
    return render(request, 'pagogastoscomues.html')
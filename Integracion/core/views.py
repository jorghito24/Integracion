from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def vistadmin(request):
    return render(request, 'vistadmin.html')

def login(request):
    return render(request, 'login.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def vistaresidente(request):
    return render(request, 'vistaresidente.html')
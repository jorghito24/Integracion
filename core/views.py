from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def vistadmin(request):
    return render(request, 'core/vistadmin.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def vistaresidente(request):
    return render(request, 'core/vistaresidente.html')

#CRUD USUARIOS

def agregarR(request):

    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            data["mensaje"] = "Guardado correctamente"
            messages.success(request, "Usuario registrado")
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'usuarios/Residentes/agregarR.html', data)

def agregarD(request):

    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            data["mensaje"] = "Guardado correctamente"
            messages.success(request, "Usuario registrado")
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'usuarios/Residentes/agregarR.html', data)

def agregarC(request):

    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            data["mensaje"] = "Guardado correctamente"
            messages.success(request, "Usuario registrado")
            return redirect(to="index")
        data["form"] = formulario

    return render(request, 'usuarios/Residentes/agregarR.html', data)
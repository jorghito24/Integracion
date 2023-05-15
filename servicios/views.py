from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.

def arriendoAC(request):
    
    servicios=Servicio.objects.all()
    return render(request, 'servicios/arriendoAC.html', {"servicios": servicios})
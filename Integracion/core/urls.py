from django.urls import path
from . import views 
from core.views import index, vistadmin,nosotros,vistaresidente, login, contacto
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    
    path('',views.index,name='index'),
    path('vistadmin/',views.vistadmin,name='vistadmin'),
    path('login/',views.login,name='login'),
    path('nosotros/',views.nosotros,name='nosotros'),
    path('vistaresidente/', views.vistaresidente, name='vistaresidente'),
    path('contacto/',views.contacto, name='contacto'),
    ]
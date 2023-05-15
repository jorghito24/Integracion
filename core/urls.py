from django.urls import path
from . import views 
from core.views import index, vistadmin,nosotros,vistaresidente, agregarR
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    
    path('',views.index,name='index'),
    path('vistadmin/',views.vistadmin,name='vistadmin'),
    path('nosotros/',views.nosotros,name='nosotros'),
    path('vistaresidente/', views.vistaresidente, name='vistaresidente'),

    #CRUD
    path('agregarR/',views.agregarR ,name='agregarR'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
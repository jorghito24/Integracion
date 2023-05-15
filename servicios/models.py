from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    descripcion=models.TextField(max_length=50)
    imagen=models.ImageField(upload_to='servicios', null=True)
    precio=models.IntegerField()
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='Servicios'

    def __str__(self):
        return self.titulo
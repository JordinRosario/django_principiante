from django.db import models
from django.contrib.auth.models import User
# Create your models here.

""" Creando la tabla de tareas """
class task(models.Model):
    title = models.CharField(max_length=100)
    descripcion =models.TextField(blank=True)
    creacion =models.DateTimeField(auto_now_add=True)
    dia_completado = models.DateTimeField(null=True)
    importante = models.BooleanField(default=True)
    """ Creamos la columna usuario donde hacemos foreng key a la tabla usuario y activamos el modo cascada """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title}, descripcion{self.descripcion} agregada por {self.user}, tarea creada {self.creacion}'
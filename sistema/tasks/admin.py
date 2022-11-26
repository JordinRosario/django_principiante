from django.contrib import admin
from .models import task 

# Register your models here.
#Agregar campo en la pantalla admin/ quitar campo
class TaskAdmin(admin.ModelAdmin):
    readonly_fields=('creacion', )

admin.site.register(task, TaskAdmin)
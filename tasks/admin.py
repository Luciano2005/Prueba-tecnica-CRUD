from atexit import register
from django.contrib import admin
from .models import Paciente, Departamento, Municipio, Genero, TipoDeDocumento

# class TasksAdmin(admin.ModelAdmin):
#     readonly_fields= ("created", ) #De esta manera le indico cuales campos son de solo lectura y que quiero ver en pantalla

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(Genero)
admin.site.register(TipoDeDocumento)

from django.forms import ModelForm
from .models import Paciente
from django import forms

class CrearPaciente(ModelForm):
    class Meta:
        model=Paciente
        fields=['nombre1','nombre2','apellido1', 'apellido2', 'genero_id','tipo_documento_id', 'numero_documento', 'departamento_id', 'municipio_id']
        widgets = {
            'nombre1' : forms.TextInput(attrs=({'placeholder':'Primer nombre'})),
            'nombre2' : forms.TextInput(attrs=({'placeholder':'Segundo nombre'})),
            'apellido1' : forms.TextInput(attrs=({'placeholder':'Primer apellido'})),
            'apellido2' : forms.TextInput(attrs=({'placeholder':'Segundo apellido'}))
        } 


        
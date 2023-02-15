from django.db import IntegrityError #Para captar este tipo de error.
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #Cuando lo ejecute me va a devolver un formulario
from django.contrib.auth.models import User  #para poder guardar los datos del usuario. "Registrarlos"
from django.contrib.auth import login, logout, authenticate #Esto es para crear la cookie que permita saber al navegador que el usuario está autenticado.
from .forms import CrearPaciente #importamos nuestro modelo de formulario
from django.utils import timezone
from django.contrib.auth.decorators import login_required #Modulo para mostrar visas solo si el usuario está logeado.
from .models import Paciente


# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request,'signup.html',{
        'form':UserCreationForm
        })
    else:
        if request.POST['password1']==request.POST['password2']:
            #Register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1']) #De esta manera creamos el usuario.

                user.save() #Acá creamos el usuario. 
                login(request, user) #Con esto creamos la cookie con la sessionID
                return redirect('home')  
            except IntegrityError:
                return render(request,'signup.html',{
                    'form':UserCreationForm,
                    'error': 'El nombre de usuario ya existe'
                })
        
        return render(request,'signup.html',{
                    'form':UserCreationForm,
                    'error':'La contraseña es incorrecta'
                })

@login_required #De esta manera le decimos a django que solo deje cargar esta vista a usuarios logeados
def lista_pacientes(request):
    lista=Paciente.objects.all()
    

    return render(request, 'lista_pacientes.html',{
        'lista': lista,
    })

@login_required 
def create_paciente(request):
    if request.method == 'GET':
        return render(request, 'create_paciente.html',{
            'form': CrearPaciente,
        })
    else:
        try:
            forms=CrearPaciente(request.POST)
            new_paciente=forms.save(commit=False) #De esta manera  guardo los datos en la base de datos
            #Es importante poner el commit en false para que aún no se guarden los datos, ya que no hemos pasado el id del usuario.
            new_paciente.user=request.user
            new_paciente.save()

            return redirect('home')

        except ValueError:
            return render(request, 'create_paciente.html',{
            'form': CrearPaciente,
            'error': 'Proporcione datos validos'
        })


@login_required 
def signout(request):
    logout(request)
    return redirect('home')
    

def signin(request):
    if(request.method == 'GET'):
        return render(request, 'login.html',{
            'form':AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None: #Si no se encontró el usuario.
            return render(request, 'login.html',{
            'form':AuthenticationForm,
            'error': 'Username or password id incorrect'
            })
        else:
            login(request, user) #Creamos una sesión
            return redirect('home')



from django.shortcuts import render

"""
FORMULARIO PARA CREAR USUARIOS
FUNCIONES PARA COMPROBAR CREDENCIALES
"""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login


def signup(request):
    #SI LA PETICION ES POST procesamos el formulario con los datos enviados
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #Logueamos automaticamente al usuario recien creado
            username=form.cleaned_data.get('username') #datos limpios del formulario
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password) #Verifica las credenciales
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})   

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from app_desafio.models import Auto, Perros, Oficinas
from app_desafio.forms import *

# Create your views here.



def inicio(request):
    return render(request, 'inicio.html')




def auto_datos(request):   
    if request.method == 'POST':
        
        mi_formulario = Autos_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            autos = Auto(marca= datos['marca'], ruedas= datos['ruedas'], creacion= datos['creacion'])
            autos.save()
       
    
    return render(request, 'auto.html')


def perros_datos(request):   
    if request.method == 'POST':

        mi_formulario = Perros_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            canino = Perros(raza= datos['raza'], edad= datos['edad'])    
            canino.save()
            return render(request, 'perros.html')

    return render(request, 'perros.html')



def oficinas_datos(request):    
    if request.method == 'POST':
        
        mi_formulario = Oficinas_formulario(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            trabajo = Oficinas(tipos= datos['tipos'], cantidad= datos['cantidad'])    
            trabajo.save()
            return render(request, 'oficinas.html')

    return render(request, 'oficinas.html')



def busqueda_autos(request):
    return render(request, 'buscar_autos.html')


def busqueda_perros(request):
    return render(request, 'buscar_perros.html')

def busqueda_oficinas(request):
    return render(request, 'buscar_oficinas.html')


def auto_busqueda(request):
    
    if request.method == 'GET':
        marca = request.GET['marca'] 
       
        autos = Auto.objects.filter(marca__icontains = marca)
        return render(request, 'resultado_autos.html', {'autos': autos})
    else:
        return HttpResponse('Campo vacio')


def perros_busqueda(request):

    if request.method == 'GET':
        raza = request.GET['raza']

        perros = Perros.objects.filter(raza__icontains = raza)
        return render(request, 'resultado_perros.html', {'perros': perros})
    else:
        return HttpResponse('Campo vacio')


def oficinas_busqueda(request):

    if request.method == 'GET':

        tipos = request.GET['tipos']

        oficinas = Oficinas.objects.filter(tipos__icontains = tipos)

        return render(request, 'resultado_oficinas.html', {'oficinas': oficinas})

    else:
        return HttpResponse('Campo vacio')

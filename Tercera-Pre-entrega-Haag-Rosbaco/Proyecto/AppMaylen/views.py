from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppMaylen.models import Curso
from AppMaylen.forms import CursoFormulario


def inicio (request) :
    return render(request, "AppMaylen/index.html")


def cursos (request) :
    return render(request, "AppMaylen/cursos.html")


def profesores (request):
    return HttpResponse ("Vista profesores")


def estudiantes (request) :
    return HttpResponse ("Vista estudiantes")


def entregables (request):
    return HttpResponse ("Vista entregables")


def curso_formulario (request) :

    if request.method == 'POST' :

        curso = Curso(
            nombre=request.POST['curso'],
            camada=request.POST['camada']
            )
        
        curso.save()

        return render(request, "AppMaylen/index.html")
    
    return render(request, "AppMaylen/curso_formulario.html")

def form_con_api(request) :
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid() :
            informacion = mi_formulario.cleaned_data

            curso = Curso (nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
        
            return render (request, "AppMaylen/index.html")
    else : 
        mi_formulario = CursoFormulario()

    return render(request, "AppMaylen/form_con_api.html", {"mi_formulario": mi_formulario})


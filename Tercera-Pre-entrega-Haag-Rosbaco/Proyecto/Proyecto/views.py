from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def inicio (request) :
    return render(request, "AppMaylen/index.html")


def cursos (request) :
    return HttpResponse ("Vista cursos")


def profesores (request):
    return HttpResponse ("Vista profesores")


def estudiantes (request) :
    return HttpResponse ("Vista estudiantes")


def entregables (request):
    return HttpResponse ("Vista entregables")
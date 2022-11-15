from django.shortcuts import render
from appcoder1.models import Curso
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, "appcoder1/index.html")
    
def cursos(request):
    return render(request, "appcoder1/cursos.html")
    
def estudiantes(request):
    return render(request, "appcoder1/estudiantes.html")
    
def profesores(request):
    return render(request, "appcoder1/profesores.html")
    
def entregables(request):
    return render(request, "appcoder1/entregables.html")
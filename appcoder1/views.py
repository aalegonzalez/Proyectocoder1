from django.shortcuts import render
from appcoder1.models import Curso, Profesor
from appcoder1.forms import ProfesorFormulario
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, "appcoder1/index.html")
    
def cursos(request):
    return render(request, "appcoder1/cursos.html")


   
def creacion_curso(request):
    if request.method == "POST":
        nombre_curso = request.POST["curso"]
        numero_camada = request.POST["camada"]
       
        curso = Curso(nombre=nombre_curso, camada=numero_camada)
        curso.save()
        
    return render(request, "appcoder1/curso_formulario.html")




def buscar_curso(request):
    return render(request, "appcoder1/busqueda_curso.html")

def resultado_busqueda_cursos(request):
    nombre_curso = request.GET["nombre_curso"]
    cursos = Curso.objects.filter(nombre__icontains=nombre_curso)
    return render(request, "appcoder1/resultado_busqueda_cursos.html", {"cursos": cursos})







def estudiantes(request):
    return render(request, "appcoder1/estudiantes.html")

def profesores(request): 
    return render(request, "appcoder1/profesores.html")



def creacion_profesores(request):
    if request.method == "POST":
        formulario = ProfesorFormulario(request.POST)

        #validamos que el formulario no tenga problemas
        if formulario.is_valid():
        #recuperamos data del atributo cleaned_data
            data = formulario.cleaned_data

            profesor = Profesor(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], profesion=data["profesion"])
            
            profesor.save()

    
    formulario = ProfesorFormulario()
    contexto = {"formulario": formulario}
    return render(request, "appcoder1/profesores_formulario.html", contexto)



    
def entregables(request):
    return render(request, "appcoder1/entregables.html")
from django.urls import path
from appcoder1.views import *


urlpatterns = [

    path("inicio/", inicio, name="coder-inicio"),

    path("estudiantes/", estudiantes, name="coder-estudiantes"),

    path("entregables/", entregables, name="coder-entregables"),


    path("profesores/", profesores, name="coder-profesores"),
    path("profesores/crear/", creacion_profesores, name="coder-profesores-crear"),


    path("cursos/", cursos, name="coder-cursos"),
    path("cursos/crear/", creacion_curso, name="coder-cursos-crear"),
    path("cursos/buscar/", buscar_curso, name="coder-cursos-buscar"),
    path("cursos/buscar/resultado/", resultado_busqueda_cursos, name="coder-cursos-buscar-resultado"),

    ]

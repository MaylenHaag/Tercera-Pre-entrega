from django.urls import path
from .views import index, create_curso, create_estudiante, create_profesor, create_entregable, curso_list, entregable_list, profesor_list, estudiante_list

urlpatterns = [
    path('', index, name='index'),
    path('crear-curso/', create_curso, name='create_curso'),
    path('cursos/', curso_list, name='curso_list'),
    path('crear-estudiante/', create_estudiante, name='create_estudiante'),
    path('estudiantes/', estudiante_list, name='estudiante_list'),
    path('crear-profesor/', create_profesor, name='create_profesor'),
    path('profesores/', profesor_list, name='profesor_list'),
    path('crear-entregable/', create_entregable, name='create_entregable'),
    path('entregables/', entregable_list, name='entregable_list'),
]
from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Profesor, Entregable
from .forms import CursoForm, EstudianteForm, ProfesorForm, EntregableForm

# Vista para la página principal con formularios y listas
def index(request):
    if request.method == 'POST':
        if 'curso_submit' in request.POST:
            form = CursoForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'estudiante_submit' in request.POST:
            form = EstudianteForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'profesor_submit' in request.POST:
            form = ProfesorForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'entregable_submit' in request.POST:
            form = EntregableForm(request.POST)
            if form.is_valid():
                form.save()

    cursos = Curso.objects.all()
    estudiantes = Estudiante.objects.all()
    profesores = Profesor.objects.all()
    entregables = Entregable.objects.all()

    return render(request, 'AppMaylen/index.html', {
        'curso_form': CursoForm(),
        'estudiante_form': EstudianteForm(),
        'profesor_form': ProfesorForm(),
        'entregable_form': EntregableForm(),
        'cursos': cursos,
        'estudiantes': estudiantes,
        'profesores': profesores,
        'entregables': entregables,
    })

# Vista para crear un curso
def create_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'AppMaylen/create_curso.html', {'form': form})

# Vista para listar cursos
def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'AppMaylen/curso_list.html', {'cursos': cursos})

# Vista para crear un estudiante
def create_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiante_list')
    else:
        form = EstudianteForm()
    return render(request, 'AppMaylen/create_estudiante.html', {'form': form})

# Vista para listar estudiantes
def estudiante_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'AppMaylen/estudiante_list.html', {'estudiantes': estudiantes})

# Vista para crear un profesor
def create_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesor_list')
    else:
        form = ProfesorForm()
    return render(request, 'AppMaylen/create_profesor.html', {'form': form})

# Vista para listar profesores
def profesor_list(request):
    profesores = Profesor.objects.all()
    return render(request, 'AppMaylen/profesor_list.html', {'profesores': profesores})

# Vista para crear un entregable
def create_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entregable_list')
    else:
        form = EntregableForm()
    return render(request, 'AppMaylen/create_entregable.html', {'form': form})

# Vista para listar entregables
def entregable_list(request):
    entregables = Entregable.objects.all()
    return render(request, 'AppMaylen/entregable_list.html', {'entregables': entregables})
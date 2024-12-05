from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyect

# Vista para listar proyectos
def list_projects(request):
    projects = Proyect.objects.all()
    return render(request, 'projects/list.html', {'projects': projects})

# Vista para crear un nuevo proyecto
def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        rut = request.POST.get('rut')
        integrantes = request.POST.get('integrantes')
        technology = request.POST.get('technology')
        Proyect.objects.create(title=title, rut=rut, integrantes=integrantes, technology=technology)
        return redirect('list_projects')
    return render(request, 'projects/create.html')

# Vista para actualizar un proyecto
def update_project(request, id):
    project = get_object_or_404(Proyect, id=id)
    if request.method == 'POST':
        project.title = request.POST.get('title')
        project.rut = request.POST.get('rut')
        project.integrantes = request.POST.get('integrantes')
        project.technology = request.POST.get('technology')
        project.save()
        return redirect('list_projects')
    return render(request, 'projects/update.html', {'project': project})

# Vista para eliminar un proyecto
def delete_project(request, id):
    project = get_object_or_404(Proyect, id=id)
    project.delete()
    return redirect('list_projects')

from .models import Project

from django.shortcuts import render, redirect
from .form import ProjectForm


def projects(request):
    projects_list = Project.objects.all()

    context = {
        'projects': projects_list
    }

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectobj = Project.objects.get(id=pk)

    return render(request, 'projects/single-projects.html', {
        'project': projectobj
    })


def CreatProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}

    return render(request, "projects/project_form.html", context)


def UpdateProject(request, pk):
    project = Project.objects.get(id=pk)

    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)

        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}

    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)

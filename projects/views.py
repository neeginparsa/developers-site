from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectobj = Project.objects.get(id=pk)
    context = {'project': projectobj}
    return render(request, 'projects/single_project.html', context)


@login_required(login_url='login')  #if user not login send user to login page
def createproject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)  #request.FILES baraye upload image tavasot karbar
        if form.is_valid:
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def updateproject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid:
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

@login_required(login_url='login')
def deleteproject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_obj.html', context)

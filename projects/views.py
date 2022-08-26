from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# projectList = [
#     {
#         'id':'1',
#         'title': "Ecommerce Website",
#         'description': 'Fully functional ecommerce website'
#     },
#     {
#         'id':'2',
#         'title': "Portfolio website",
#         'description': 'This was a project where I built out my portfolio'
#     },
#     {
#         'id':'3',
#         'title': "Social network",
#         'description': 'Awesome open project I am still working'
#     },
# ]

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj =  Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/Single-project.html', { 'project': projectObj, 'tags': tags })

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form= ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = { 'form': form }
    return render(request, 'projects/project_form.html', context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form= ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = { 'form': form }
    return render(request, 'projects/project_form.html', context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method== 'POST':
        project.delete()
        return redirect('projects')
    context ={'object': project}
    return render(request, 'projects/delete_template.html', context)
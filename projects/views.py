# projects/views.py

from django.shortcuts import render
from projects.models import Projects

# Create your views here.

def projects_index(request):
    projects = Projects.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/projects_index.html", context)

def projects_detail(request, pk):
    projects = Projects.objects.get(pk=pk)
    context = {
        "projects": projects
    }
    return render(request, "projects/projects_detail.html", context)



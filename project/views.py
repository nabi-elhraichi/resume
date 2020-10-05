from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request,'project/index.html', context)

def detail(request,project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project': project
    }

    return render(request,'project/detail.html', context)


def projectForm(request):
    form = ProjectForm(request.POST or None)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form
    }

    return render(request,'project/form.html', context)


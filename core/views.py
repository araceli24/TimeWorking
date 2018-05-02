import datetime

from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from .forms import ProjectForm
from .models import Project, ActivityJournal


# Create your views here.

@login_required
def project_list(request):
    journals = ActivityJournal.objects.filter(end__isnull=True, user=request.user)
    projects = Project.objects.filter(user=request.user)
    return render(request, 'core/project_list.html', {'projects': projects, 'journals': journals})


class ProjectDetail(DetailView):

    template_name = "core/project_detail.html"
    model = Project

  
@login_required
def project_new(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'core/project_edit.html', {'form': form})

@login_required
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'core/project_edit.html', {'form': form})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('project_list')


@login_required
def project_start(request, pk):

    #now = datetime.datetime.now()
    activities = ActivityJournal.objects.filter(
        end__isnull=True, user=request.user)
    activities.update(end=timezone.now())
    proyecto = Project.objects.get(id=pk)
    a = ActivityJournal(start=timezone.now(),
                        user=request.user, project=proyecto)

    a.save()

    return redirect('project_list')
    #ActivityJournal.objects.get(end__isnull=True, user=request.user)


@login_required
def project_stop(request, pk):

    # pasar proyecto y que pare ese proyecto
    proyecto = Project.objects.get(id=pk)
    activities = ActivityJournal.objects.filter(
        end__isnull=True, user=request.user)
    activities.update(end=timezone.now())

    proyecto.save()

    return redirect('project_list')



class LoginWithCheckIn(LoginView):


    def form_valid(self, form):
    
    
        context= super() .form_valid(form)   

        #check in

        return context
        

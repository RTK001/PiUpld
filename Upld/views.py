from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import GitHubProject
from .forms import *
from .platformio_interface import *

class IndexView(generic.ListView):
    template_name = "Upld/index.html"
    model = GitHubProject

    def get_context_data(self, **kwargs):
        ''' added available devices to context'''
        context = super().get_context_data(**kwargs)
        context['devices'] = get_devices()
        print(context)
        return context

    def get_queryset(self):
        ''' return a list of all projects'''
        print(GitHubProject.objects.all())
        return GitHubProject.objects.all()


class ProjectCreateView(generic.edit.CreateView):
    form_class = NewProjectForm
    model = GitHubProject
    template_name = "Upld/ProjectCreate.html"
    success_url = reverse_lazy("Upld:index")

from django.shortcuts import render
from django.views import generic
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
        return GitHubProject.objects.all()


class ProjectCreateView(generic.edit.CreateView):
    form_class = NewProjectForm

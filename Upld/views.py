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
        context['streamed'] = StreamingHttpResponse(WriteToDevice()).streaming_content
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




from django.http import StreamingHttpResponse
import subprocess

class iteratorTest():
    def __init__(self):
        pass
    def __iter__(self):
        self.proc = subprocess.Popen(["ping", "192.168.0.5", "-t"],
                                    stdout=subprocess.PIPE,
                                    shell=True,
                                    universal_newlines = True,
                                    bufsize=1)
        return self
    def __next__(self):
        for line in self.proc.stdout:
            return "<br>" + line



class StreamingTest(generic.ListView):
    template_name = 'Upld/StreamingTest.html'
    def get_queryset(self, **kwargs):
        return None

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            response = StreamingHttpResponse(WriteToDevice())
            return response
        else:
            return super(StreamingTest, self).dispatch(request, *args, **kwargs)

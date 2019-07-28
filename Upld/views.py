from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import project
from .platformio_interface import *

class IndexView(TemplateView):
    template_name = "Upld/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['devices'] = get_devices()
        print(context)
        return context

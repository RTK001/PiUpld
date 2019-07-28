from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import project

class IndexView(TemplateView):
    template_name = "Upld/index.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

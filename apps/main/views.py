from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView

from apps.tort.models import Tort
from apps.flour.models import Flour


class HomeView(TemplateView):
    template_name = 'index.html'
    context_object_name = 'main'


class AboutView(TemplateView):
    template_name = 'about.html'
    context_object_name = 'about'


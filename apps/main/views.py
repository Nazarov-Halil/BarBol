from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from apps.tort.models import Tort
from apps.flour.models import Flour

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tort_list'] = Tort.objects.all()[:8]  # Получаем первые 8 элементов из модели Tort
        context['flour_list'] = Flour.objects.all()[:8]  # Получаем первые 8 элементов из модели Flour
        return context


class AboutView(TemplateView):
    template_name = 'barbol/about.html'
    context_object_name = 'about'

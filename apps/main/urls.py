from django.urls import path
from apps.main.views import HomeView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='main_list'),
    path('about', AboutView.as_view(), name='about_list')
]
from django.urls import path
from apps.tort.views import TortListView, TortDetailView
urlpatterns = [
    path('tort', TortListView.as_view(), name='tort_list'),
    path('tort/<int:pk>/', TortDetailView.as_view(), name='tort_detail'),


]

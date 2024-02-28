from django.urls import path
from apps.flour.views import FlourListView,FlourDetailView

urlpatterns = [
    path('flour', FlourListView.as_view(), name='flour_list'),
    path('flour/<int:pk>', FlourDetailView.as_view(), name='flour_detail')
]
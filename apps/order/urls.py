from django.urls import path
from apps.order.views import CreateOrderView, OrderListView

urlpatterns = [
    path('order', CreateOrderView.as_view(), name='order'),
    path('happy', OrderListView.as_view(), name='happy')
]
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from pyexpat.errors import messages

from apps.order.forms import OrderForm
from apps.order.models import Order


class OrderListView(ListView):
    template_name = 'barbol/happy_bay.html'
    context_object_name = 'happy_bay_list'

    def get_queryset(self):
        return Order.objects.all()


class CreateOrderView(CreateView):
    form_class = OrderForm
    template_name = 'flour-html/../../templates/barbol/bay.html'
    success_url = reverse_lazy('happy')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
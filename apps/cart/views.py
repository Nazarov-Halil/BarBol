from django.shortcuts import render, redirect
from django.views.generic import ListView

from apps.cart.models import Cart



class CartListViews(ListView):
    model = Cart
    template_name = 'cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Cart.objects.all()

class QuantityChangeLogics:
    @staticmethod
    def minus_quantity(request, pk):
        item = Cart.objects.get(id=pk)
        if item.quantity - 1 == 0:
            item.delete()
            return redirect('cart_list')
        item.quantity -= 1
        item.save()
        return redirect('cart_list')

    @staticmethod
    def pilus_quantity(request, pk):
        item = Cart.objects.get(id=pk)
        item.quantity += 1
        item.save()
        return redirect('cart_list')
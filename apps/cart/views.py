from django.db.models import Q, QuerySet
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView

from apps.cart.models import Card, CardItem, CardItemFlour
from apps.flour.models import Flour
from apps.tort.models import Tort


class CartListViews(ListView):
    model = Card
    template_name = 'barbol/cart.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Card.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     carts = self.get_queryset()
    #     total_sum = Card.get_total_sum(carts)
    #     context['total_sum'] = total_sum
    #     return context


class QuantityChangeLogics:
    @staticmethod
    def minus_quantity(request, pk):
        item = CardItem.objects.get(id=pk)
        if item.quantity - 1 == 0:
            item.delete()
            return redirect('detail_card')
        item.quantity -= 1
        item.save()
        return redirect('detail_card')

    @staticmethod
    def pilus_quantity(request, pk):
        item = CardItem.objects.get(id=pk)
        item.quantity += 1
        item.save()
        return redirect('detail_card')
class QuantityChangeLogicsFlour:
    @staticmethod
    def minus_quantity_flour(request, pk):
        item = CardItemFlour.objects.get(id=pk)
        if item.quantity - 1 == 0:
            item.delete()
            return redirect('detail_card')
        item.quantity -= 1
        item.save()
        return redirect('detail_card')

    @staticmethod
    def pilus_quantity_flour(request, pk):
        item = CardItemFlour.objects.get(id=pk)
        item.quantity += 1
        item.save()
        return redirect('detail_card')


def create_cart_item(request, pk):
    hash = request.session.get("_auth_user_hash")

    if Card.objects.filter(user_session=hash).exists():
        card = Card.objects.get(user_session=hash)
    else:
        card = Card.objects.create(
            user_session=hash
        )

    tort = Tort.objects.get(id=pk)
    CardItem.objects.create(
        card=card,
        tort=tort,
    )

    return redirect('tort_detail', tort.id)


def create_cart_item_flour(request, pk):
    hash = request.session.get("_auth_user_hash")
    if Card.objects.filter(user_session=hash).exists():
        card = Card.objects.get(user_session=hash)
    else:
        card = Card.objects.create(
            user_session=hash
        )
    flour = Flour.objects.get(id=pk)
    CardItemFlour.objects.create(
        card=card,
        flour=flour,
    )

    return redirect('flour_detail', flour.id)


def detail_card(request):
    card = Card.objects.get(user_session=request.session.get("_auth_user_hash"))
    all_items = list(card.items.all())+list(card.flours_items.all())

    return render(request, 'barbol/cart.html', locals())

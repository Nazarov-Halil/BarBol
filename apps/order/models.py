from django.contrib.auth.models import User
from django.db import models
from apps.cart.views import Card


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(
        Card, on_delete=models.CASCADE,
        related_name='cart_order',
        null=True, blank=True
    )
    name = models.CharField(
        max_length=50,
        verbose_name='Имя'
    )
    email = models.EmailField(
        verbose_name='Электронная почта'

    )
    phone = models.CharField(
        max_length=10,
        verbose_name='Телфон номер:'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

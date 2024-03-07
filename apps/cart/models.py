from django.db import models
from apps.flour.models import Flour
from apps.tort.models import Tort


# class Cart(models.Model):
#     tort = models.ForeignKey(
#         Tort, on_delete=models.CASCADE,
#         related_name='carts',
#         blank=True,
#         null=True,
#     )
#     flour = models.ForeignKey(
#         Flour, on_delete=models.CASCADE,
#         related_name='carts',
#         null=True,
#         blank=True,
#     )
#     quantity = models.PositiveSmallIntegerField(
#         default=1, verbose_name='Каличество'
#     )
#
#     def sum_quantity(self):
#         if self.tort:
#             return int(self.quantity * self.tort.price)
#         elif self.flour:
#             return int(self.quantity * self.flour.price)
#         else:
#             return 0
#
#     @staticmethod
#     def get_total_sum(carts):
#         total_sum = 0
#         for cart in carts:
#             total_sum += cart.sum_quantity()
#         return total_sum
#
#     def __str__(self):
#         return f'{self.tort},{self.flour}'
#
#     class Meta:
#         verbose_name = 'Избранный'
#         verbose_name_plural = 'Избранные'


class Card(models.Model):
    user_session = models.CharField(
        max_length=120,
        verbose_name="Сессия пользователя",
    )

    def get_total(self):
        return sum(item.sum_quantity() for item in list(self.flours_items.all()) + list(self.items.all()))



    def __str__(self):
        return self.user_session


class CardItem(models.Model):
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Корзина",
    )
    tort = models.ForeignKey(
        Tort, on_delete=models.CASCADE,
        related_name="cards",
        verbose_name="Торт",
    )
    quantity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Количество",
    )

    def sum_quantity(self):
        return int(self.quantity * self.tort.price)

    def __str__(self):
        return f'{self.tort.title}'


class CardItemFlour(models.Model):
    card = models.ForeignKey(
        Card, on_delete=models.CASCADE,
        verbose_name='Карзина',
        related_name="flours_items",
    )
    flour = models.ForeignKey(
        Flour, on_delete=models.CASCADE,
        related_name='cards',
        verbose_name='Мучное',
    )
    quantity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Количество'
    )

    def sum_quantity(self):
        return int(self.quantity * self.flour.price)

    def __str__(self):
        return self.flour.title

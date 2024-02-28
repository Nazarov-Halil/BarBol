from django.db import models
from apps.flour.models import Flour
from apps.tort.models import Tort


class Cart(models.Model):
    tort = models.ForeignKey(
        Tort, on_delete=models.CASCADE,
        related_name='tort',
        blank=True,
        null=True,
    )
    flour = models.ForeignKey(
        Flour, on_delete=models.CASCADE,
        related_name='flour',
        null=True,
        blank=True,
    )
    quantity = models.PositiveSmallIntegerField(
        default=1, verbose_name='Каличество'
    )

    def sum_quantity(self):
        return int(self.quantity * f'{self.tort.price},{self.flour.price}')

    def get_total_sum(self):
        sum_price = sum(i.get_price() for i in self.tort.price.all())
        sum_flour_price = sum(i.get_price() for i in self.flour.price.all())
        return sum_price, sum_flour_price

    def __str__(self):
        return f'{self.tort},{self.flour}'

    class Meta:
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранные'

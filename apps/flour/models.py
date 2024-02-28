from django.db import models
import os
from utils.image_path import upload_images


class Flour(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    flour_image = models.ImageField(
        upload_to=upload_images,
        verbose_name='Картинка'
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.flour_image.path)
        super().delete(using=using, keep_parents=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мучной'
        verbose_name_plural = "Мучные"
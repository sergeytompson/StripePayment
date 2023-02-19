from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField("Название товара", max_length=100)
    description = models.TextField("Описание товара", blank=True, null=True)
    price = models.PositiveIntegerField("Цена товара")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("pet", kwargs={"pk": self.pk})

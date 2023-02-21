from django.db import models
from django.urls import reverse

from .validators import is_positive


class Item(models.Model):
    CURRENCIES = [("rub", "рублей"), ("usd", "долларов")]
    name = models.CharField("Название товара", max_length=100)
    description = models.TextField("Описание товара", blank=True, null=True)
    price = models.PositiveIntegerField("Цена товара")
    currency = models.CharField(
        "Валюта", choices=CURRENCIES, max_length=3, default="rub"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("item", kwargs={"pk": self.pk})


class Tax(models.Model):
    display_name = models.CharField("Короткое название", max_length=50)
    inclusive = models.BooleanField("Включается ли в стоимость", default=False)
    percentage = models.DecimalField(
        "Налоговая ставка",
        max_digits=6,
        decimal_places=4,
        validators=[
            is_positive,
        ],
    )

    class Meta:
        verbose_name = "Налог"
        verbose_name_plural = "Налоги"

    def __str__(self) -> str:
        return self.display_name


class Discount(models.Model):
    percent_off = models.DecimalField(
        "Скидка",
        max_digits=3,
        decimal_places=1,
        validators=[
            is_positive,
        ],
    )

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"

    def __str__(self) -> str:
        return str(self.percent_off)


class Order(models.Model):
    items = models.ManyToManyField(Item)
    tax = models.ForeignKey(Tax, on_delete=models.SET_NULL, blank=True, null=True)
    discount = models.ForeignKey(
        Discount, on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self) -> str:
        return "Заказ №" + str(self.pk)

from django.http import HttpRequest

from .models import Order


def get_order(request: HttpRequest) -> dict[str, Order]:
    order, _ = Order.objects.get_or_create(pk=1)
    return {"order": order}

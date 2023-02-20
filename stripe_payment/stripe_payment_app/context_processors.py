from .models import Order


def get_order(request):
    order, _ = Order.objects.get_or_create(pk=1)
    return {"order": order}

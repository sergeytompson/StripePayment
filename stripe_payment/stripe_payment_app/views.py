from django import http
from django.db.models import QuerySet
from django.views.generic import DetailView, View

from stripe_payment_app.utils.session import get_session

from .models import Item, Order

CURRENCY_MAP = {
    "rub": "₽",
    "usd": "$",
}


class ItemDetailView(DetailView):
    model = Item
    context_object_name = "item"

    def get_object(self, queryset: QuerySet = None) -> Item:
        obj = super().get_object()
        obj.price /= 100
        obj.currency = CURRENCY_MAP[obj.currency]
        return obj


class BuyView(View):
    def get(self, request: http.HttpRequest, pk: int) -> http.JsonResponse:
        item = Item.objects.get(pk=pk)
        session = get_session([item])
        return http.JsonResponse(session)


class OrderView(DetailView):
    model = Order
    queryset = Order.objects.prefetch_related("items")
    context_object_name = "this_order"

    def get_object(self, queryset: QuerySet = None) -> Order:
        obj = super().get_object()
        for item in obj.items.all():
            item.price /= 100
            item.currency = CURRENCY_MAP[item.currency]
        return obj


class ItemToOrderView(View):
    def get(
        self, request: http.HttpRequest, order_pk: int, item_pk: int
    ) -> http.JsonResponse:
        order = Order.objects.get(pk=order_pk)
        item = Item.objects.get(pk=item_pk)
        if order.items.count() and order.items.first().currency != item.currency:
            return http.JsonResponse(
                {"data": "Нельзя добавлять в заказ товары с разной валютой в стоимости"}
            )
        order.items.add(item)
        return http.JsonResponse({"message": "Товар добавлен в заказ"})


class BuyOrderView(View):
    def get(self, request: http.HttpRequest, pk: int) -> http.JsonResponse:
        order = Order.objects.prefetch_related("items").get(pk=pk)
        tax = order.tax
        discount = order.discount
        items = order.items.all()
        session = get_session(items, tax, discount)
        order.delete()
        return http.JsonResponse(session)

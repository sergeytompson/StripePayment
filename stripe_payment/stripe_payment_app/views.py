from django import http
from django.http import HttpResponse
from django.views.generic import DetailView, View

from .models import Item, Order

from utils.session import get_session


class ItemDetailView(DetailView):
    model = Item
    context_object_name = "item"

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.price /= 100
        return obj


class BuyView(View):

    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        session = get_session([item])
        return http.JsonResponse(session)


class OrderView(DetailView):
    model = Order
    queryset = Order.objects.prefetch_related('items')
    context_object_name = "this_order"

    def get_object(self, queryset=None):
        obj = super().get_object()
        for item in obj.items.all():
            item.price /= 100
        return obj


class ItemToOrderView(View):

    def get(self, request, order_pk, item_pk):
        Order.objects.get(pk=order_pk).items.add(Item.objects.get(pk=item_pk))
        return HttpResponse()


class BuyOrderView(View):

    def get(self, request, pk):
        order = Order.objects.prefetch_related('items').get(pk=pk)
        tax = order.tax
        discount = order.discount
        items = order.items.all()
        session = get_session(items, tax, discount)
        order.delete()
        return http.JsonResponse(session)

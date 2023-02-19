import os
import stripe

from django import http
from django.views.generic import DetailView, View

from .models import Item


stripe.api_key = os.environ.get("STRIPE_IP_KEY")


class ItemDetailView(DetailView):
    model = Item
    context_object_name = "item"

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.price = obj.price / 100
        return obj


class BuyView(View):

    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'rub',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
        )
        return http.JsonResponse(session)

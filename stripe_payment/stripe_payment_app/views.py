import os
import stripe

from django import http
from django.views.generic import DetailView

from .models import Item


stripe.api_key = os.environ.get("STRIPE_IP_KEY")


class ItemDetailView(DetailView):
    model = Item
    context_object_name = "item"


def get_session_id(request, pk):
    session = stripe.checkout.Session.create(
        line_items=[{
          'price_data': {
            'currency': 'usd',
            'product_data': {
              'name': 'T-shirt',
            },
            'unit_amount': 2000,
          },
          'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success',
      )
    return http.JsonResponse(session)

import os
from copy import deepcopy

import stripe

ITEM_FORM = {
    'price_data': {
        'currency': 'rub',
        'product_data': {
            'name': None,
        },
        'unit_amount': None,
    },
    'quantity': 1,
}

stripe.api_key = os.environ.get("STRIPE_IP_KEY")


def get_session(items):
    line_items = []
    for item in items:
        item_form = deepcopy(ITEM_FORM)
        item_form['price_data']['product_data']['name'] = item.name
        item_form['price_data']['unit_amount'] = item.price
        line_items.append(item_form)
    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode='payment',
        success_url='http://localhost:8000/success',
    )
    return session

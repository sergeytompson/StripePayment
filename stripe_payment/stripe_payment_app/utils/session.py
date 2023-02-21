import os
from copy import deepcopy
from typing import Union

import stripe

from stripe_payment_app.models import Discount, Tax

ITEM_FORM = {
    "price_data": {
        "currency": None,
        "product_data": {
            "name": None,
        },
        "unit_amount": None,
    },
    "quantity": 1,
}

stripe.api_key = os.environ.get("STRIPE_IP_KEY")


def get_session(
    items, tax: Union[Tax, None] = None, discount: Union[Discount, None] = None
) -> stripe.checkout.Session:
    line_items = []

    tax_rate = None
    if tax:
        tax_rate = stripe.TaxRate.create(
            display_name=tax.display_name,
            inclusive=tax.inclusive,
            percentage=tax.percentage,
        )

    for item in items:
        item_form = deepcopy(ITEM_FORM)
        item_form["price_data"]["product_data"]["name"] = item.name
        item_form["price_data"]["currency"] = item.currency
        item_form["price_data"]["unit_amount"] = item.price
        if tax_rate:
            item_form["tax_rates"] = [tax_rate.id]
        line_items.append(item_form)

    discounts = None
    if discount:
        coupon = stripe.Coupon.create(percent_off=discount.percent_off)
        discounts = [
            {
                "coupon": coupon.id,
            }
        ]

    session = stripe.checkout.Session.create(
        line_items=line_items,
        mode="payment",
        discounts=discounts,
        success_url="http://localhost:8000/item/1",
    )
    return session

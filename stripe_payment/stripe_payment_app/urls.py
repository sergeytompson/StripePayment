from django.urls import path

from .views import ItemDetailView, BuyView, OrderView, ItemToOrderView, BuyOrderView

urlpatterns = [
    path('item/<int:pk>', ItemDetailView.as_view(), name='item'),
    path('buy/<int:pk>', BuyView.as_view(), name='buy'),
    path('order/<int:pk>', OrderView.as_view(), name='order'),
    path('add_item_to_order/<int:order_pk>/<int:item_pk>', ItemToOrderView.as_view(), name='item_to_order'),
    path('order_buy/<int:pk>', BuyOrderView.as_view(), name='order_buy'),
]

from django.urls import path

from .views import ItemDetailView, BuyView

urlpatterns = [
    path('item/<int:pk>', ItemDetailView.as_view(), name='item'),
    path('buy/<int:pk>', BuyView.as_view(), name='buy'),
]

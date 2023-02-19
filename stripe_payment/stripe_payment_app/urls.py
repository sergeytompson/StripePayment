from django.urls import path

from .views import ItemDetailView, get_session_id

urlpatterns = [
    path('item/<int:pk>', ItemDetailView.as_view(), name='item'),
    path('buy/<int:pk>', get_session_id, name='buy'),
]

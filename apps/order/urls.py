from django.urls import path
from apps.order.views import add_to_cart, cart_button

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart-button/', cart_button, name='cart_button'),
]
from django.urls import path
from apps.order.views import add_to_cart, cart_button, create_order_view

urlpatterns = [
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('cart-button/', cart_button, name='cart_button'),
    path('creat/', create_order_view, name='create_order'),
]
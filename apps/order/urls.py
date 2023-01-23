from django.urls import path
from apps.order.views import set_to_cart

urlpatterns = [
    path('add-to-cart/', set_to_cart, name='add_to_cart'),
]
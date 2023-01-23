from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.order.forms import AddToCartForm
from apps.order.models import Cart


# Create your views here.
def gat_car_data(user):
    total = 0
    cart = Cart.objects.filter(user=user).select_related('product')
    for row in cart:
        total += row.quantity * row.product.price
    return {'total': total, 'cart': cart}


@login_required
def set_to_cart(request):
    data = request.GET.copy()
    data.update(user=request.user)
    request.GET = data
    form = AddToCartForm()
    if form.is_valid():
        cd = form.cleaned_data
        row = Cart.objects.filter(user=cd['user'],product=cd['product'])
        if row:
            Cart.objects.filter(id=row).update(quantity=row+cd['quantity'])
        else:
            form.save()
        return render(request,'order/added.html',{"product":cd['product'],"cart": gat_car_data[cd['user']]})
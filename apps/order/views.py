from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from apps.order.forms import AddToCartForm, CreatOrderForm
from apps.order.models import Cart


# Create your views here.
def get_car_data(user):
    total = 0
    cart = Cart.objects.filter(user=user).select_related('product')
    for row in cart:
        total += row.quantity * row.product.price
    return {'total': total, 'cart': cart}


@login_required
def add_to_cart(request):
    data = request.GET.copy()
    data.update(user=request.user)
    request.GET = data
    form = AddToCartForm(request.GET)
    if form.is_valid():
        cd = form.cleaned_data
        row = Cart.objects.filter(user=cd['user'],product=cd['product']).first()
        if row:
            Cart.objects.filter(id=row.id).update(quantity=row.quantity + cd['quantity'])
        else:
            form.save()
        breadcrumbs = {
            reverse('cart_button'): 'Корзина',
            'current': 'Добавлено'
        }
        return render(request,'order/added.html',{"product":cd['product'],'breadcrumbs':breadcrumbs, "cart": get_car_data(cd['user'])})


@login_required
def cart_button(request):
    breadcrumbs = {
        'current': 'Корзина'
    }
    return render(request, 'order/button.html',{"cart": get_car_data(request.user.id),"breadcrumbs":breadcrumbs})

@login_required
def create_order_view(request):
    error = None
    user = request.user
    cart = get_car_data(user)
    if not cart['cart']:
        return redirect('index')
    if request.method == 'POST':
        data = request.POST.copy()
        data.update(user=user,total=cart['total'])
        request.POST = data

        form = CreatOrderForm(request.POST)
        if form.is_valid():
            form.save()
            Cart.objects.filter(user=user).delete()
            return render(request,'order/created.html')
        error = form.errors
    else:
        form = CreatOrderForm(data={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone if user.phone else ''
        })
    breadcrumbs = {
        reverse('cart_button'): 'Корзина',
        'current': 'Оформления'
    }
    return render(request,'order/create.html', {'cart':cart,'error':error,'form':form,'breadcrumbs':breadcrumbs})


from .forms import CartItemForm
from .models import Cart, Product, Cartitem
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    form = CartItemForm()
    context = {'product': product, 'form': form}
    return render(request, 'product_detail.html', context)


def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    form = CartItemForm(data=request.POST)
    if form.is_valid():
        Cart.objects.get_or_create(user=request.user)
        user_cart = Cart.objects.get(user=request.user)
        try:
            item = Cartitem.objects.filter(cart=user_cart).get(name=product.name)
        except:
            new_item = form.save(commit=False)
            new_item.name = product.name
            new_item.price = product.price
            new_item.cover = product.cover
            new_item.cart = user_cart
            new_item.save()
        else:
            add_num = form.save(commit=False)
            item.quantity += add_num.quantity
            item.save()
        return redirect('djancommerce:product_detail', product_id=product_id)
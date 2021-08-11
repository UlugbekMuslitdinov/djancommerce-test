from .forms import CartItemForm
from .models import Cart, Product, Cartitem
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    user_cart = Cart.objects.get(user=request.user)
    form = CartItemForm()
    context = {'product': product, 'form': form, 'cart': user_cart}
    return render(request, 'product_detail.html', context)


def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)
    form = CartItemForm(data=request.POST)
    if form.is_valid():
        Cart.objects.get_or_create(user=request.user)
        user_cart = Cart.objects.get(user=request.user)
        try:
            item = Cartitem.objects.filter(cart=user_cart).get(prod_id=product.id)
        except Cartitem.DoesNotExist:
            new_item = form.save(commit=False)
            new_item.name = product.name
            new_item.price = product.price
            new_item.cover = product.cover
            new_item.cart = user_cart
            new_item.prod_id = product.id
            new_item.save()
        else:
            add_num = form.save(commit=False)
            item.quantity += add_num.quantity
            item.save()
        return redirect('djancommerce:product_detail', product_id=product_id)


def cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = Cartitem.objects.filter(cart=cart)
    form = CartItemForm(instance=Cartitem)
    context = {'cart': cart, 'cart_items': cart_items, 'form': form}
    return render(request, 'cart.html', context)


def item_update(request, item_id):
    item = Cartitem.objects.get(id=item_id)
    form = CartItemForm(data=request.POST)
    new_num = form.save(commit=False)
    item.quantity = new_num.quantity
    item.save()
    return redirect('djancommerce:cart')


def item_delete(request, item_id):
    item = Cartitem.objects.get(id=item_id)
    item.delete()
    return redirect('djancommerce:cart')
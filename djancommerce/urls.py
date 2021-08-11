from django.urls import path
from .views import *

app_name = 'djancommerce'

urlpatterns = [
    path('<str:product_id>/detail/', product_detail, name='product_detail'),
    path('<str:product_id>/cart-add/', cart_add, name='cart_add'),
    path('cart/', cart, name='cart'),
    path('<str:item_id>/update/', item_update, name='item_update'),
    path('<str:item_id>/delete/', item_delete, name='item_delete'),
    path('create-order/', create_order, name='create_order'),
]
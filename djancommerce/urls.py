from django.urls import path
from .views import *

app_name = 'djancommerce'

urlpatterns = [
    path('<str:product_id>/detail/', product_detail, name='product_detail'),
    path('<str:product_id>/cart_add/', cart_add, name='cart_add'),
]
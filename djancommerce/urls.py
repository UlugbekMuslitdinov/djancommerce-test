from django.urls import path
from .views import *

app_name = 'djancommerce'

urlpatterns = [
    path('new-category', new_category, name='new_category'),
]
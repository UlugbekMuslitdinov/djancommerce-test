from django.contrib import admin
from .models import *


class ProductInline(admin.TabularInline):
    model = Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ("name",)}
    inlines = [ProductInline,]


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'created_at',]
    sortable_by = ['price', 'category']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'cart', 'price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    cover = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='product/')
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f'{self.user}'

    def total_items_by_quantity(self):
        return sum(item.quantity for item in self.cartitem_set.all())

    def total_items_by_product_type(self):
         return len(self.cartitem_set.all())

    def total_price(self):
        return sum(item.price * item.quantity for item in self.cartitem_set.all())


class Cartitem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    cover = models.ImageField(upload_to='product/')
    prod_id = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.name} + {self.id}'


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, choices=settings.PAYMENT_METHODS)
    delivery_method = models.CharField(max_length=50, choices=settings.DELIVERY_METHODS)
    status = models.CharField(max_length=50, choices=settings.DELIVERY_STATUSES, default='To be confirmed')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='product/')
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
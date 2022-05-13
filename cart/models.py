from django.db import models
from django.contrib.auth.models import User
from products.models import Products



class Cart(models.Model):
    session_key = models.CharField(max_length=999, blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    total_cost = models.PositiveIntegerField()
    

    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        items = CartContent.objects.filter(cart=self.id)
        total = 0
        for item in items:
            total += item.product.price * item.qty
        return total

    @property
    def get_cart_content(self):
        return CartContent.objects.filter(cart=self.id)


class CartContent(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(null=True)

import uuid # univeisally unique identifier
from django.db import models
from products.models import Product
# Create your models here.

class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
    quantity = models.PositiveIntegerField(default=1)

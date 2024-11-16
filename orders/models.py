from django.conf import settings
from django.db import models

from products.models import Product

# Create your models here.

class Order(models.Model):
    
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Completed'),
        (PAYMENT_STATUS_FAILED, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    pending_status = models.CharField(max_length=55, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=False, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.pending_status
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return self.product.name
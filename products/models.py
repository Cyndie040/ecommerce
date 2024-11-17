from django.db import models
from accounts.models import User
from categories.models import Category

# to import store, user and category

# Create your models here.

"""
it will have the following for database model
class Product:
    name
    description
    category
    price
    quantity
    imageurl
    updated 
    created at
"""

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products_catergory', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    quantity = models.PositiveIntegerField(null=False, default=0)
    imageUrl = models.URLField()
    Created_by = models.ForeignKey(User, default=True, related_name='product_owner', on_delete=models.CASCADE)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)  # Track how many times the product is viewed
    # store_id = models.ForeignKey(Store, related_name="store", on_delete=models.CASCADE)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return '{} {}'.format(self.name, self.price)
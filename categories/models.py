from django.db import models

# Create your models here.

#name = models.CharField(max_length
# description = models.TextField(blank=True, null=True)
class Category(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title
    
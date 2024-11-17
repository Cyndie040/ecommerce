from django.db import models
import secrets
from django.contrib.auth.models import User
from .paystack import Paystack
from django.conf import settings


# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.IntegerField(blank=True, null=True)
    ref = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.user} + {self.amount}'
    
    def save(self, *args, **kwargs):
        
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            
            if not object_with_similar_ref.exists():
                self.ref = ref
        
        super().save(*args, **kwargs)
        
    
    def amount_value(self):
        return int(self.amount) * 100
    
    def verify_payment(self):
        paystack = Paystack()
        pending_status, transaction_data = paystack.verify_payment(self.ref, self.amount)
        
        # if pending_status == 'success':
        #     self.verified = True
        #     self.save()
        #     return True
        
        # return False
        
        if pending_status:
            
            if transaction_data['amount'] / 100 == self.amount:
                self.verified = True
                self.save()
        
        if self.verified:
            return True
        else:
            return False
        
            
        
    

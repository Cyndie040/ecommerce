from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

# for customer user manager
class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        
        user = self.model(
            email=email,
            **extra_fields
        )
        
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser has to have is_staff being true')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser has to have is_superuser being true')
        
        return self.create_user(email=email, password=password, **extra_fields)
    
   
   #custom user model 
class User(AbstractUser):
    email = models.CharField(max_length=70, unique=True)
    username = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    
    objects=CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username

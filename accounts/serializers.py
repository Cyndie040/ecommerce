from rest_framework import serializers
from .models import User
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

class SignupSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        # extra_kwargs = {'password': {'write_only': True}}
        
    def validate(self, attrs):
        
        email_exists = User.objects.filter(email=attrs['email']).exists()
        
        if email_exists:
            raise ValidationError('Email already exists')
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        
        user = super().create(validated_data)
        
        user.set_password(password)
        
        user.save()
        
        Token.objects.create(user=user)
        
        return user
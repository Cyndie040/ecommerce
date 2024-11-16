from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ['id', 'placed_at', 'pending_status']
        

class CreateOrderSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    
    def save(self, **kwargs):
        cart_id = self.validated_data['cart_id']
        return super().save(**kwargs)
from rest_framework import serializers
from .models import Product


# class ProductSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     quantity = serializers.IntegerField()
#     created_at = serializers.DateTimeField(read_only=True)

# to be used always 
class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200, allow_blank=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'created_at']
        # fields = '__all__'  # all fields in the model
        
        

    
    
    
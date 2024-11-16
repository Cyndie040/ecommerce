from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Order
from orders.serializers import CreateOrderSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework import status, generics, mixins
# from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class CustomPaginator(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'page_size'

# using model mixins
class OrderListCreateView(generics.GenericAPIView, 
                             mixins.ListModelMixin, 
                             mixins.CreateModelMixin):
    """
        a view for creating orders list
    """
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # queryset = Order.objects.all().order_by('title')
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    
    
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class OrderRetrieveUpdateDeleteView(generics.GenericAPIView,
                                       mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin):
    
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
        





# class OrderViewSet(ModelViewSet):
#     # serializer_class = OrderSerializer
#     """
#         a view for creating a category list
#     """
#     queryset = Order.objects.all()
#     permission_classes = [IsAuthenticated]
    
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return CreateOrderSerializer
#         return OrderSerializer
        
    
#     def get_queryset(self):
#         user = self.request.user
#         if user.is_staff:
#             return Order.objects.all()
#         return Order.objects.filter(owner=user)
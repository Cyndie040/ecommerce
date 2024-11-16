from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet

# Create your views here.
from django.shortcuts import render
from rest_framework.request import Request
from rest_framework import status, generics, mixins
from .models import Cart
from .serializers import CartSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
# from rest_framework.decorators import api_view, APIView, permission_classes
# from  .permissions import ReadOnly, AuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class CustomPaginator(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'page_size'

# using model mixins
class CartListCreateView(generics.GenericAPIView, 
                             mixins.ListModelMixin, 
                             mixins.CreateModelMixin):
    """
        a view for creating a cart list
    """
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    
    @swagger_auto_schema(
        operation_summary='Listing all cart items',
        operation_description='This returns a list of all cart items'
    )
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='Creates cart items',
        operation_description='This creates list of all cart items'
    )
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class CartRetrieveUpdateDeleteView(generics.GenericAPIView,
                                       mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin):
    
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    
    @swagger_auto_schema(
        operation_summary='Retrieve all cart items',
        operation_description='This retrieves a list of all cart items'
    )
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='Updates all cart items',
        operation_description='This updates all cart items'
    )
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='Delete cart items by id',
        operation_description='This deletes cart items by a given id'
    )
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
        



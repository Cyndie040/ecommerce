from django.shortcuts import render
from rest_framework.request import Request
from rest_framework import status, generics, mixins
from .models import Category
from .serializers import CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.decorators import api_view, APIView, permission_classes
# from  .permissions import ReadOnly, AuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class CustomPaginator(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'page_size'

# using model mixins
class CategoryListCreateView(generics.GenericAPIView, 
                             mixins.ListModelMixin, 
                             mixins.CreateModelMixin):
    """
        a view for creating a category list
    """
    serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    queryset = Category.objects.all().order_by('title')
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    
    @swagger_auto_schema(
        operation_summary='To list categories',
        operation_description='This endpoint will list all categories'
    )
    
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='To create categories',
        operation_description='This endpoint will create categories'
    )
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class CategoryRetrieveUpdateDeleteView(generics.GenericAPIView,
                                       mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin):
    
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    
    @swagger_auto_schema(
        operation_summary='To retrieve categories',
        operation_description='This endpoint will retrieve a category based on its id'
    )
    
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='To update categories',
        operation_description='This endpoint will update a category based on its id'
    )
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='To delete categories',
        operation_description='This endpoint will delete a category based on its id'
    )
    
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
        



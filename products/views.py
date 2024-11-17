from django.shortcuts import render
# from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView, permission_classes # for both function and class based views
from .models import Product, Category
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from  .permissions import ReadOnly, AuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination
from categories.serializers import CategorySerializer
from drf_yasg.utils import swagger_auto_schema



# for filtering in django
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter

# for searching  and ordering in django
from rest_framework.filters import SearchFilter, OrderingFilter
from payments.models import Payment
from django.conf import settings


class CustomPaginator(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'page_size'

# for viewset based views
from rest_framework import viewsets, status
from rest_framework.request import Request
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from .models import Product
# from products.serializers import ProductSerializer


# Create your views here.

# def homepage(request:HttpRequest):
#     response = {'message': 'Welcome to Ecommerce site project'}
#     return JsonResponse(data=response)

# products = [
#     {
#         'id':1,
#         'title': 'Products on Electronics', 
#         'content': 'This is the first post'
#     },
#     {
#         'id':2,
#         'title': 'Products on Cosmetics', 
#         'content': 'This is the second post'
#     },
#     {
#         'id':3,
#         'title': 'Products on Beauty', 
#         'content': 'This is the third post'
#     },
#     {
#         'id':4,
#         'title': 'Products on gadgets', 
#         'content': 'This is the fourth post'
#     }
# ]


# function based views
@api_view(http_method_names=['GET', 'POST'])
@permission_classes([AllowAny])
def homepage(request:Request):
    
    if request.method == 'POST':
        data = request.data
        
        response = {'message': 'Welcome to Ecommerce site project', 'data': data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    
    response = {'message': 'Welcome to Ecommerce site project'}
    return Response(data=response, status=status.HTTP_200_OK)

class ListProductForAuthor(
    generics.GenericAPIView,
    mixins.ListModelMixin
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        username = self.request.query_params.get('username') or None
        
        queryset = Product.objects.all()
        
        if username is not None:
           return Product.objects.filter(author__username=username)
       
        return queryset
        
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# @api_view(http_method_names=['GET', 'POST'])
# def list_products(request:Request):
#     products = Product.objects.all()
    
#     if request.method == 'POST':
#         data = request.data
        
#         serializer = ProductSerializer(data=data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             response={
#                 'message': 'Product created successfully',
#                 'data': serializer.data
#             }
            
#             return Response(data=response, status=status.HTTP_201_CREATED)
        
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     serializer = ProductSerializer(instance=products, many=True)
    
#     response = {
#         'message':'products',
#         'data': serializer.data
#     }
    
#     return Response(data=response, status=status.HTTP_200_OK)

# @api_view(http_method_names=['GET'])
# def product_detail(request:Request, product_id: int):
#     product = get_object_or_404(Product, pk=product_id)
    
#     serializer = ProductSerializer(instance=product)
    
#     response = {
#         'message':'product',
#         'data': serializer.data
#     }
#     return Response(data=response, status=status.HTTP_200_OK)
    

# @api_view(http_method_names=['PUT'])
# def update_product(request: Request, product_id:int):
#     product = get_object_or_404(Product, pk=product_id)
    
#     data = request.data
    
#     serializer = ProductSerializer(instance=product, data=data)
    
#     if serializer.is_valid():
#         serializer.save()
        
#         response={
#             'message': 'Product updated successfully',
#             'data': serializer.data
#         }
        
#         return Response(data=response, status=status.HTTP_200_OK)
    
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(http_method_names=['DELETE'])
# def delete_product(request: Request, product_id:int):
#     product = get_object_or_404(Product, pk=product_id)
    
#     product.delete()
    
#     response = {
#         'message': 'Product deleted successfully',
#         'data': {}
#     }
    
#     return Response(data=response, status=status.HTTP_204_NO_CONTENT)


# class based views

# class ProductListCreateView(APIView):
#     """
#         a view for creating and listing products
#     """
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request, *args, **kwargs):
#         products = Product.objects.all()
        
#         serializer = self.serializer_class(instance=products, many=True) # the many=true will help return a list of products in json format
    
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     def post(self, request, *args, **kwargs):
#         data = request.data 
        
#         serializer = self.serializer_class(data=data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             response = {
#                 'message': 'Product created successfully',
#                 'data': serializer.data
#             }
            
#             return Response(data=response, status=status.HTTP_201_CREATED)
        
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class ProductRetrieveUpdateDeleteView(APIView):
#     """
#         a view for retrieving, updating, and deleting a product
#     """
#     serializer_class = ProductSerializer
#     permission_classes = [IsAuthenticated]
    
#     def get(self, request:Request, product_id:int):
#         product = get_object_or_404(Product, pk=product_id)
        
#         serializer = self.serializer_class(instance=product)
        
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request:Request, product_id:int):
#         product = get_object_or_404(Product, pk=product_id)
        
#         data = request.data
        
#         serializer = self.serializer_class(instance=product, data=data)
        
#         if serializer.is_valid():
#             serializer.save()
            
#             response={
#                 'message': 'Product updated successfully',
#                 'data': serializer.data
#             }
            
#             return Response(data=response, status=status.HTTP_200_OK)
        
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request:Request, product_id:int):
#         product = get_object_or_404(Product, pk=product_id)
        
#         product.delete()
        
#         response = {
#             'message': 'Product deleted successfully',
#             'data': {}
#         }
        
#         return Response(data=response, status=status.HTTP_204_NO_CONTENT)
    

# for generics apiview and mixins
class ProductListCreateView(generics.GenericAPIView,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    
    """
#         a view for listing all products
#     """
    
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CustomPaginator
    queryset = Product.objects.all()
    
    @swagger_auto_schema(
        operation_summary='Listing all products',
        operation_description='This returns a list of all products'
    )
    
    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        return super().perform_create(serializer)
    
    @swagger_auto_schema(
        operation_summary='Listing all products',
        operation_description='This returns a list of all products'
    )
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='Create a product',
        operation_description='This create a products'
    )
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ProductRetrieveUpdateDeleteView(generics.GenericAPIView,
                                      mixins.RetrieveModelMixin,
                                      mixins.UpdateModelMixin,
                                      mixins.DestroyModelMixin):
    
    """
#         a view for retrieving, updating, and deleting a product
#     """
    
    serializer_class = ProductSerializer
    permission_classes = [AuthorOrReadOnly]
    queryset = Product.objects.all()
    
    @swagger_auto_schema(
        operation_summary='This endpoint retrieves product by id',
        operation_description='This retrives products by an id'
    )
    
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_summary='This endpoint updates products by id',
        operation_description='This updates products by id'
    )
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    
    @swagger_auto_schema(
        operation_summary='This deletes products by id',
        operation_description='This delete products by id'
    )
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        
    
# viewset based views
# class ProductViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
    
#     def list(self, request:Request):
#         queryset = Product.objects.all()
#         serializer = ProductSerializer(instance=queryset, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
#     def retrieve(self, request:Request, pk=None):
#         product = get_object_or_404(Product, pk=pk)
        
#         serializer = ProductSerializer(instance=product)
        
#         return Response(data=serializer.data, status=status.HTTP_200_OK)


# # for model viewsets
# class ProductViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
#     filterset_class = ProductFilter
#     search_fields = ['name', 'description']
#     ordering_fields = ['price', 'created_at']
    
    

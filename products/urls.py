from . import views
from django.urls import path

urlpatterns = [
    path('homepage/', views.homepage, name='products_home'),
    # path('', views.list_products, name='list_products'), # for function based views
    # path('<int:product_id>/', views.product_detail, name = 'product_detail'),
    # path('update/<int:product_id>/', views.update_product, name = 'product_update'),
    # path('delete/<int:product_id>/', views.delete_product, name = 'product_delete'),
    
    # urls for class based views
    path('', views.ProductListCreateView.as_view(), name = 'products_list'), # for class base views
    path('<int:pk>/', views.ProductRetrieveUpdateDeleteView.as_view(), name = 'products_retrieve'),
    path('products_for/', views.ListProductForAuthor.as_view(), name = 'product_for_current_user'),
]

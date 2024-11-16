from . import views
from django.urls import path

urlpatterns = [
    path('', views.CategoryListCreateView.as_view(), name = 'category_list'),
    path('<int:pk>/', views.CategoryRetrieveUpdateDeleteView.as_view(), name = 'category_retrieve'),# for class base views
]
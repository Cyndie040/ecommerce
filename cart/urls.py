from . import views
from django.urls import path

urlpatterns = [
    path('', views.CartListCreateView.as_view(), name = 'cart_list'),
    path('<int:pk>/', views.CartRetrieveUpdateDeleteView.as_view(), name = 'cart_retrieve'),# for class base views
]
# from . import views
# from django.urls import path

# urlpatterns = [
#     path('', views.OrderViewSet.as_view(), name = 'orders'),
# ]

from . import views
from django.urls import path

urlpatterns = [
    path('', views.OrderListCreateView.as_view(), name = 'category_list'),
    path('<int:pk>/', views.OrderRetrieveUpdateDeleteView.as_view(), name = 'category_retrieve'),
]
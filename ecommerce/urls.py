"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

# for viewsets
# from products.views import ProductViewSet
from rest_framework.routers import DefaultRouter
# from orders.views import OrderViewSet

...
# from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

if settings.DEBUG:
    schema_view = get_schema_view(
            openapi.Info(
               title="Ecommerce_web API",
               description="This is an API for ecommerce website",
               default_version="1.0",
               contact=openapi.Contact(email="admin@app.com"),
               license=openapi.License(name="BSD License"),
            ),
            public=True,
            permission_classes=(permissions.AllowAny,),
        )
else:
    schema_view = get_schema_view(
        openapi.Info(
            title="Ecommerce_web API",
            description="This is an API for ecommerce website",
            default_version="1.0",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
        url="https://web-ecommerce-site.up.railway.app/"
    )




router=DefaultRouter()

# router.register('', ProductViewSet, basename='products')

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('admin/', admin.site.urls),
#    path('products/', include(router.urls)), # for router urls
   path('auth/', include('accounts.urls')),
   path('categories/', include('categories.urls')),
   path('cart/', include('cart.urls')),
   path('orders/', include('orders.urls')),
   path('products/', include('products.urls')),
    # path('orders/', include(router.urls)), # for router urls
    
]



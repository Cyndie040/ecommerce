from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from . views import ProductListCreateView
from django.contrib.auth import get_user_model
# Create your tests here.


User = get_user_model()

class HelloWorldTestCase(APITestCase):
    
    def test_hello_world(self):
        response = self.client.get(reverse('products_home'))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Welcome to Ecommerce site project')
        

class ProductListCreateTestCase(APITestCase):
    
    def setUp(self):
    #     self.factory= APIRequestFactory()
    #     self.view = ProductListCreateView.as_view()
    #     # self.url = reverse('product_list_create')
        self.url = reverse('products_list')
    #     self.user = User.objects.create(
    #         username='Cynthia',
    #         email='cynthia@gmail.com',
    #         password='password##123'
    #     )
        
    def authenticate(self):
        
        self.client.product(reverse('signup'), {
            'email':'cynarios@gmail.com',
            'password':'password##123',
            'username':'cynarios'
        })
        
        response = self.client.product(reverse('login'),{
            'email':'cynarios@gmail.com',
            'password':'password##123',
        })
        print(response.data)
        token = response.data['tokens']['access']
        
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    def test_list_products(self):
        
        response = self.client.get(self.url)
        
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'],0)
        self.assertEqual(response.data['results'], [])
    
    def test_product_creation(self):
        # sample_post = {
        #     'name': 'iphone 14',
        #     'description': 'Is the newest device available'
        # }
        # request = self.factory.post(self.url, sample_post)
        # request.user = self.user
        
        # response = self.view(request)
        
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.authenticate()
        
        sample_data = {
            'name':'sample name',
            'description':'sample description'
        }
        
        response = self.client.product(reverse('products_list'),sample_data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], sample_data['name'])
from django.urls import path
from .views import *

app_name = "cart"

urlpatterns = [
   path('add_product/<int:product_id>/', add_product, name='add_product'),
   path('remove_product/<int:product_id>/', remove_product, name='remove_product'),
   path('decrement_product/<int:product_id>/', decrement_product, name='decrement_product'),
   path('clear/', clear_cart, name='clear_cart'),
   
   path('add_procesador/<int:product_id>/', add_procesador, name='add_procesador'),
   path('remove_procesador/<int:product_id>/', remove_procesador, name='remove_procesador'),
   path('decrement_procesador/<int:product_id>/', decrement_procesador, name='decrement_procesador'),
   path('clear_procesador/', clear_cart_procesador, name='clear_cart_procesador'),
   
   path('add_gpu/<int:product_id>/', add_gpu, name='add_gpu'),
   path('remove_gpu/<int:product_id>/', remove_gpu, name='remove_gpu'),
   path('decrement_gpu/<int:product_id>/', decrement_gpu, name='decrement_gpu'),
   path('clear_gpu/', clear_cart_gpu, name='clear_cart_gpu'),
   
   path('add_ram/<int:product_id>/', add_ram, name='add_ram'),
   path('remove_ram/<int:product_id>/', remove_ram, name='remove_ram'),
   path('decrement_ram/<int:product_id>/', decrement_ram, name='decrement_ram'),
   path('clear_ram/', clear_cart_ram, name='clear_cart_ram'),
   
]
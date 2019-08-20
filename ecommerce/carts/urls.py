from django.urls import path, re_path
from .views import cart_home, cart_update, checkout_home

app_name = 'cart'
urlpatterns = [
    path('', cart_home, name='home'),
    path('update/', cart_update, name='update'),
    path('checkout/', checkout_home, name='checkout'),
    
]


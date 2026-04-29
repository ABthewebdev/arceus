from django.urls import path
from .views import *
from accounts.views import *


urlpatterns = [
    path('', home, name='home'),
    path('business/', business_dashboard, name='business_dashboard'),
    path('browse/', browse_food, name='browse_food'),
    path('food/', food_list, name='food_list'),
    path('food/add/', add_food, name='add_food'),
    path('orders/', orders, name='orders'),
    path('rewards/', rewards, name='rewards'),
    path('menu/', menu, name='menu'),
]
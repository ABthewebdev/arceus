from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse_food, name='browse_food'),
    path('restaurant/', views.restaurant_dashboard, name='restaurant_dashboard'),
    path('restaurant/add/', views.add_restaurant, name='add_restaurant'),
    path('food/', views.food_list, name='food_list'),
    path('food/add/', views.add_food, name='add_food'),
    path('food/<int:pk>/order/', views.order_food, name='order_food'),
    path('api/dropdown-menu/', views.dropdown_menu, name='dropdown_menu'),
    path('orders/', views.orders_view, name='orders'),
    path('rewards/', views.rewards_view, name='rewards'),
    path('menu/', views.menu_view, name='menu'),
]
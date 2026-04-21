from django.contrib import admin
from .models import Restaurant, Food, Order

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'phone', 'created_at')
    search_fields = ('name', 'address')

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price', 'quantity', 'available')
    list_filter = ('available', 'restaurant')
    search_fields = ('name', 'description')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'food', 'customer', 'status', 'quantity', 'created_at')
    list_filter = ('status',)
    search_fields = ('food__name', 'customer__username')

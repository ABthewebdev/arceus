from django.contrib import admin
from .models import Restaurant, Food, Order

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Order)
# class RestaurantAdmin(admin.ModelAdmin):
#     list_display = ('name', 'user', 'phone', 'created_at')
#     search_fields = ('name', 'address')

# class FoodAdmin(admin.ModelAdmin):
#     list_display = ('name', 'restaurant', 'price', 'quantity', 'available')
#     list_filter = ('available', 'restaurant')
#     search_fields = ('name', 'description')

# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'food', 'customer', 'status', 'quantity', 'created_at')
#     list_filter = ('status',)
#     search_fields = ('food__name', 'customer__username')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .models import *
from accounts.models import *

def home(request):
    return render(request, 'home.html')

def browse_food(request):
    foods = Food.objects.filter(available=True, quantity__gt=0).select_related('business').order_by('-created_at')
    return render(request, 'browse_food.html', {'foods': foods})

def food_list(request):
    business = get_object_or_404(Business, user=request.user)
    foods = Food.objects.filter(business=business)
    return render(request, 'food_list.html', {'foods': foods})

def add_food(request):
    business = get_object_or_404(Business, user=request.user)
    
    if request.method == 'POST':
        food = Food.objects.create(
            business=business,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            quantity=int(request.POST.get('quantity', 1)),
            price=request.POST.get('price'),
            original_price=request.POST.get('original_price') or None,
            pickup_start=request.POST.get('pickup_start'),
            pickup_end=request.POST.get('pickup_end'),
            available=True,
        )
        messages.success(request, f'Food "{food.name}" added successfully!')
        return redirect('food_list')
    
    return render(request, 'add_food.html')



def orders(request):
    """Handle Orders click"""
    return render(request, 'pages/orders.html')


def rewards(request):
    """Handle Rewards click"""
    return render(request, 'pages/rewards.html')


def menu(request):
    """Handle Menu click"""
    return render(request, 'pages/menu.html')

def order_food(request, pk):
    food = get_object_or_404(Food, pk=pk, available=True)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > food.quantity:
            messages.error(request, 'Requested quantity exceeds available quantity.')
            return redirect('browse_food')
        
        order = Order.objects.create(
            food=food,
            customer=request.user,
            quantity=quantity,
            notes=request.POST.get('notes', ''),
        )
        food.quantity -= quantity
        if food.quantity <= 0:
            food.available = False
        food.save()
        
        messages.success(request, f'Order placed successfully! Order #{order.id}')
        return redirect('my_orders')
    
    return render(request, 'order_food.html', {'food': food})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Restaurant, Food, Order


def home(request):
    if request.user.is_authenticated:
        try:
            restaurant = request.user.restaurant
            return redirect('restaurant_dashboard')
        except Restaurant.DoesNotExist:
            pass
    return render(request, 'home.html')


@login_required
def browse_food(request):
    foods = Food.objects.filter(available=True, quantity__gt=0).select_related('restaurant').order_by('-created_at')
    return render(request, 'browse_food.html', {'foods': foods})


@login_required
def restaurant_dashboard(request):
    try:
        restaurant = request.user.restaurant
    except Restaurant.DoesNotExist:
        messages.error(request, 'You need to create a restaurant profile first.')
        return redirect('add_restaurant')
    
    foods = Food.objects.filter(restaurant=restaurant)
    pending_orders = Order.objects.filter(
        food__restaurant=restaurant,
        status__in=['pending', 'confirmed', 'ready']
    ).select_related('food', 'customer')
    
    return render(request, 'restaurant_dashboard.html', {
        'restaurant': restaurant,
        'foods': foods,
        'pending_orders': pending_orders,
    })


@login_required
def food_list(request):
    restaurant = get_object_or_404(Restaurant, user=request.user)
    foods = Food.objects.filter(restaurant=restaurant)
    return render(request, 'food_list.html', {'foods': foods})


@login_required
def add_food(request):
    restaurant = get_object_or_404(Restaurant, user=request.user)
    
    if request.method == 'POST':
        food = Food.objects.create(
            restaurant=restaurant,
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


@login_required
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


@login_required
def my_orders(request):
    orders = Order.objects.filter(customer=request.user).select_related('food__restaurant').order_by('-created_at')
    return render(request, 'my_orders.html', {'orders': orders})


@login_required
def update_order_status(request, pk):
    order = get_object_or_404(Order, food__restaurant__user=request.user, pk=pk)
    
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(request, f'Order #{order.id} status updated to {new_status}.')
    
    return redirect('restaurant_dashboard')


@login_required
def add_restaurant(request):
    if request.method == 'POST':
        restaurant = Restaurant.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            address=request.POST.get('address'),
            phone=request.POST.get('phone'),
            description=request.POST.get('description', ''),
        )
        messages.success(request, 'Restaurant profile created successfully!')
        return redirect('restaurant_dashboard')
    
    return render(request, 'add_restaurant.html')
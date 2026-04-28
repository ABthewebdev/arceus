from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomerRegisterForm, BusinessRegisterForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def customer_register(request):
    if request.method == "POST":
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
    else:
        form = CustomerRegisterForm()

    return render(request, "accounts/customer_register.html", {"form": form})

def customer_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )

        if user and user.user_type == "Customer":
            login(request, user)
            return redirect("Customer_dashboard")

    return render(request, "accounts/customer_login.html")

def business_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )

        if user and user.user_type == "business":
            login(request, user)
            return redirect("business_dashboard")

    return render(request, "accounts/business_login.html")

def business_register(request):
    if request.method == "POST":
        form = BusinessRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('business_dashboard')
    else:
        form = BusinessRegisterForm()

    return render(request, "accounts/business_register.html", {"form": form})

def business_dashboard(request):
    return render(request, 'login/business_login.html')
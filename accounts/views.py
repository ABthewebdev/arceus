from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomerRegisterForm, BusinessRegisterForm
from django.contrib.auth.forms import AuthenticationForm

def customer_register(request):
    if request.method == "POST":
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
    else:
        form = CustomerRegisterForm()

    return render(request, "registration/customer_register.html", {"form": form})

def customer_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            email=request.POST["email"],
            password=request.POST["password"],
        )

        if user and user.user_type == "Customer":
            login(request, user)
            return redirect("Customer_dashboard")

    return render(request, "login/customer_login.html")


def business_register(request):
    if request.method == "POST":
        form = BusinessRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('business_dashboard')
    else:
        form = BusinessRegisterForm()

    return render(request, "registration/business_register.html", {"form": form})

def business_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            email=request.POST["email"],
            password=request.POST["password"],
        )

        if user and user.user_type == "business":
            login(request, user)
            return redirect("business_dashboard")

    return render(request, "login/business_login.html")

def business_dashboard(request):
    return render(request, 'business_dashboard.html')
# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("customer/register/", views.customer_register, name="customer_register"),
    path("business/register/", views.business_register, name="business_register"),
    path("customer/login/", views.customer_login, name="customer_login"),
    path("business/login/", views.business_login, name="business_login"),
]
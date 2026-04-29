from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class UserType(models.TextChoices):
        CUSTOMER = "customer", "Customer"
        BUSINESS = "business", "Business"

    user_type = models.CharField(max_length=20, choices=UserType.choices)


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.first


class Business(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=255)
    business_description = models.TextField(blank=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.BigIntegerField(max_length=5)
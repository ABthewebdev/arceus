# accounts/forms.py
from django import forms
from .models import CustomUser, Customer, Business

class CustomerRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["email", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = "CUSTOMER"
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
            Customer.objects.create(user=user)

        return user


class BusinessRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    business_name = forms.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ["email", "password", "business_name"]

    def save(self, commit=True):
        user = CustomUser(
            email=self.cleaned_data["email"],
            user_type="BUSINESS",
        )
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
            Business.objects.create(
                user=user,
                business_name=self.cleaned_data["business_name"],
            )

        return user
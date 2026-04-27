from django import forms
from django.contrib.auth.models import User
from .models import Restaurant


class RestaurantRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    
    # Restaurant fields
    name = forms.CharField(max_length=255, label='Restaurant Name')
    address = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=20)
    description = forms.CharField(widget=forms.Textarea, required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already in use.')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned_data

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
        )
        restaurant = Restaurant.objects.create(
            user=user,
            name=self.cleaned_data['name'],
            address=self.cleaned_data['address'],
            phone=self.cleaned_data['phone'],
            description=self.cleaned_data.get('description', ''),
        )
        return user

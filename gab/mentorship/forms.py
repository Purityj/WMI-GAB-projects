from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={
        'class': 'block w-full px-4 py-2 text-lg rounded-lg border-gray-300 focus:ring-green-500 focus:border-green-500',
        'placeholder': 'Enter your email'
    }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'block w-full px-4 py-2 text-lg rounded-lg border-gray-300 focus:ring-green-500 focus:border-green-500',
        'placeholder': 'Enter your password'
    }))

from django import forms
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    full_name = forms.CharField()
    phone = forms.CharField()
    address = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
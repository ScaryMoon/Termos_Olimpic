from django import forms
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    full_name = forms.CharField()
    phone = forms.RegexField(
    regex=r'^\+375\d{9}$',
    error_messages={
        'invalid': 'Введите номер в формате +375291234567'
    },
    widget=forms.TextInput(
        attrs={
            'placeholder': '+375291234567'
        }
    )
)
    address = forms.CharField(
    widget=forms.Textarea(
        attrs={
            'placeholder': 'Например: г. Минск, ул. Ленина, д. 10, кв. 15',
            'rows': 3
        }
    )
)
    email = forms.EmailField(
    widget=forms.EmailInput(
        attrs={
            'placeholder': 'example@gmail.com'
        }
    )
)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
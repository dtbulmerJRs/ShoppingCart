__author__ = 'Julian Khandros'

from django import forms
from django.contrib.auth.forms import UserCreationForm


USER_TYPE = (
    ('Customer', 'Customer'),
    ('Merchant', 'Merchant'),
)


class ShoppingCartUserForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=USER_TYPE)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)
__author__ = 'Julian Khandros'

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

"""
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
"""


USER_TYPE = (
       ('Customer', 'Customer'),
       ('Merchant', 'Merchant'),
)


class ShoppingCartUserForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=USER_TYPE)

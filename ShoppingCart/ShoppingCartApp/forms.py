__author__ = 'Julian Khandros'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from ShoppingCartApp.models import Product


USER_TYPE = (
    ('Customer', 'Customer'),
    ('Merchant', 'Merchant'),
)


class ShoppingCartUserForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=USER_TYPE)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)


class AddToCartForm(forms.ModelForm):
    def __init__(self, product, *args, **kwargs):
        prod = forms.ChoiceField(choices=product)

"""
class AddToCartForm(forms.ModelForm):
    def __init__(self, products, *args, **kwargs):
        super(AddToCartForm, self).__init__(*args, **kwargs)
        self.fields['prods'] = forms.ModelChoiceField(queryset=products)

    class Meta:
        model = Product
"""
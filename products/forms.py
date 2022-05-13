from django.forms import ModelForm, TextInput, Textarea
from django import forms

from .models import Products

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['images', 'name', 'about', 'companys', 'cotegory', 'price']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'Название блюда'
            }),
            "about": Textarea(attrs={
                'class': 'form-group',
                'placeholder': 'О блюде'
            }),
            "cotegory": TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'Тип блюда'
            }),
        }

class SearchForm(forms.Form):
    search = forms.CharField(required=False,
                             label='', )
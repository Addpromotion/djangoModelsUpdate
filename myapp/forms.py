from django import forms
from .models import Customer, Product, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'photo']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
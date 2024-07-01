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

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Price cannot be negative")
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative")
        return quantity


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
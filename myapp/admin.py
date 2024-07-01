from django.contrib import admin
from .models import Customer, Product, Order
from .forms import ProductForm

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'registration_date')
    search_fields = ('name', 'email', 'phone')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('name', 'description', 'price', 'quantity', 'date_added')
    search_fields = ('name',)
    list_filter = ('date_added',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'total_amount', 'order_date')
    search_fields = ('customer__name',)
    list_filter = ('order_date',)
    filter_horizontal = ('products',)
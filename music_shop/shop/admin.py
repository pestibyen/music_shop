from django.contrib import admin

from .models import Category, SubCategory, Product, Client, Order, OrderItem, New
admin.site.register((Category, SubCategory, Product, Client, Order, OrderItem, New))

# Register your models here.

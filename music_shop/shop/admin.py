from django.contrib import admin

from .models import Category, SubCategory, Product, Client, Order, OrderItem, News
admin.site.register((Category, SubCategory, Product, Client, Order, OrderItem, News))

# Register your models here.

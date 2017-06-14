from django.contrib import admin

from .models import Category, SubCategory, Product, Address, Client, Order, OrderItem, Photo, New
admin.site.register((Category, SubCategory, Product, Address, Client, Order, OrderItem, Photo, New))

# Register your models here.

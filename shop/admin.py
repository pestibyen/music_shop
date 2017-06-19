from django.contrib import admin
from .models import Category, SubCategory, Product, Address, Profile, Order, OrderItem, Photo, News
admin.site.register((Category, SubCategory, Product, Address, Profile, Order, OrderItem, Photo, News))

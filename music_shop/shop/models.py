# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)


class SubCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    category_id = models.ForeignKey(Category)


class Products(models.Model):
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='product_images')
    description = models.TextField()
    subcategory_id = models.ForeignKey(SubCategory)

# Create your models here.

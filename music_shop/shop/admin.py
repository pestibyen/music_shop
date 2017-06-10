# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, SubCategory, Products
admin.site.register((Category, SubCategory, Products))
# Register your models here.

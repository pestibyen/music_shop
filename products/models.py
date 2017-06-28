from django.db import models
from categories.models import SubCategory


class Product(models.Model):
    name = models.CharField(max_length=50, default='')
    manufacturer = models.CharField(max_length=40, default='', blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(upload_to='product/', blank=True)
    description = models.TextField(default='', blank=True)
    subcategory = models.ForeignKey(SubCategory)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    name = models.CharField(max_length=30, unique=True)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

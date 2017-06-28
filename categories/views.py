from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product
from .models import Category, SubCategory


class CatalogView(ListView):
    template_name = 'base_catalogs.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(CatalogView, self).get_context_data(**kwargs)
        context['catalogs'] = Category.objects.values('id', 'name')
        context['catalogactive'] = Category.objects.values('id', 'name').filter(id=self.kwargs.get('catid'))
        context['subcatalogs'] = SubCategory.objects.values('id', 'name').filter(category_id=self.kwargs.get('catid'))
        subcatalogs_id = SubCategory.objects.values('id').filter(category_id=self.kwargs.get('catid'))
        context['cat_list'] = Product.objects.values('id', 'name', 'price', 'photo', 'description').filter(subcategory_id__in=subcatalogs_id)
        for i in context['cat_list']:
            i['photo'] = Photo.objects.filter(id__in=i['photo'].split(','))
        return context


class SubCatalogView(ListView):
    template_name = 'base_subcatalogs.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(SubCatalogView, self).get_context_data(**kwargs)
        context['catalogs'] = Category.objects.values('id', 'name')
        context['catalogactive'] = Category.objects.values('id', 'name').filter(id=self.kwargs.get('catid'))
        context['subcatalogs'] = SubCategory.objects.values('id', 'name').filter(category_id=self.kwargs.get('catid'))
        context['subcatalogactive'] = SubCategory.objects.values('id', 'name').filter(id=self.kwargs.get('subcatid'))
        context['cat_list'] = Product.objects.values('id', 'name', 'price', 'photo', 'description').filter(subcategory_id=self.kwargs.get('subcatid'))
        for i in context['cat_list']:
            i['photo'] = Photo.objects.filter(id__in=i['photo'].split(','))
        return context

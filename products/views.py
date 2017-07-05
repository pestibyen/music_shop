from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import AddingProductForm
from .models import Product
from categories.models import Category, SubCategory
from main.mixins import CategoryViewMixin


class Addproduct(PermissionRequiredMixin, FormView, CategoryViewMixin):
    permission_required = 'user.is_staff'
    template_name = 'product_add.html'
    form_class = AddingProductForm
    success_url = '/success/'

    def form_valid(self, form):
        name_handler = form.cleaned_data['name']
        manufacturer_handler = form.cleaned_data['manufacturer']
        price_handler = form.cleaned_data['price']
        subcategory_handler = form.cleaned_data['subcategory']
        description_handler = form.cleaned_data['description']
        photo_handler = form.cleaned_data['photo']
        Product.objects.create(name=name_handler, manufacturer=manufacturer_handler,
                               price=price_handler, subcategory=subcategory_handler,
                               description=description_handler, photo=photo_handler)
        return super(Addproduct, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Addproduct, self).get_context_data(**kwargs)
        return context


def success(request):
    return render(request, 'success.html')


class ProductView(ListView):
    template_name = 'product.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['catalogs'] = Category.objects.values('id', 'name')
        context['catalogactive'] = Category.objects.values('id', 'name').filter(id=self.kwargs.get('catid'))
        context['subcatalogs'] = SubCategory.objects.values('id', 'name').filter(category_id=self.kwargs.get('catid'))
        context['subcatalogactive'] = SubCategory.objects.values('id', 'name').filter(id=self.kwargs.get('subcatid'))
        context['item'] = Product.objects.values('id', 'name', 'price', 'photo', 'description', 'manufacturer').filter(id=self.kwargs.get('itemid'))
        # for i in context['cat_list']:
        #     i['photo'] = Photo.objects.filter(id__in=i['photo'].split(','))
        return context

from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import AddingProductForm
from .models import Product
from categories.models import Category


class Addproduct(PermissionRequiredMixin, FormView):
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
        context['catalogs'] = Category.objects.values('id', 'name')
        return context


def success(request):
    return render(request, 'success.html')

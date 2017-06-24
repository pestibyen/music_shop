from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.views.generic.base import View
from .forms import RegistrationForm, AddingProductForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Photo, Product, News, Category, SubCategory


class IndexView(ListView):
    template_name = 'index.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['catalogs'] = Category.objects.values('id', 'name')
        return context


class CatalogView(ListView):
    template_name = 'products/base_catalogs.html'
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
    template_name = 'products/base_subcatalogs.html'
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


class Registration(FormView):
    template_name = 'users/registration.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        form.cleaned_data['email'] = form.cleaned_data['username']
        new_user = User.objects.create_user(**form.cleaned_data)
        login(self.request, new_user)
        return super(Registration, self).form_valid(form)


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


def success(request):
    return render(request, 'users/success.html')


class Addproduct(PermissionRequiredMixin, FormView):
    permission_required = 'user.is_staff'
    template_name = 'staff/addproduct.html'
    form_class = AddingProductForm
    success_url = '/success/'

    def form_valid(self, form):
        f1 = form.cleaned_data['name']
        f2 = form.cleaned_data['manufacturer']
        f3 = form.cleaned_data['price']
        f4 = form.cleaned_data['subcategory']
        f5 = form.cleaned_data['description']
        p1 = form.cleaned_data['photo1']
        p2 = form.cleaned_data['photo2']
        p3 = form.cleaned_data['photo3']
        p4 = form.cleaned_data['photo4']
        p5 = form.cleaned_data['photo5']
        photo_li, photo_list, photo_list_id = list(), list(), list()

        for i in (p5, p4, p3, p2, p1):
            if i and i not in photo_list:
                photo_li.append(i)

        for i in photo_li:
            a = i.replace('\\', '/')
            x = a.find('/images/')
            y = a[x+1:]
            photo_list.append(y)

        for i in range(0, len(photo_list)):
            f6_db, created = Photo.objects.get_or_create(filename=photo_list[i])

            if created:
                f6_db_id = Photo.objects.values('id').filter(filename=photo_list[i])[0]['id']
            else:
                f6_db_id = Photo.objects.values('id').filter(filename=f6_db)[0]['id']

            photo_list_id.append(str(f6_db_id))

        photo_str_id = ','.join(photo_list_id)
        Product.objects.create(name=f1, manufacturer=f2,
                               price=f3, subcategory=f4,
                               description=f5, photo=photo_str_id)
        return super(Addproduct, self).form_valid(form)
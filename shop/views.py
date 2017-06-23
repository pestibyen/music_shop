from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.base import View
from .forms import RegistrationForm, AddingProductForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from .models import Photo, Product


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class Registration(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        form.cleaned_data['email'] = form.cleaned_data['username']
        new_user = User.objects.create_user(**form.cleaned_data)
        login(self.request, new_user)
        return super(Registration, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
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


class Addproduct(FormView):
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
        photo_list, photo_list_id = list(), list()

        for i in (p5, p4, p3, p2, p1):
            if i and i not in photo_list:
                photo_list.append(i)

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

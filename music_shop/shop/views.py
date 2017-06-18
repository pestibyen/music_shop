from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import RegistrationForm, AddingProductForm
from .models import Client, Photo, Product


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context


class Registration(FormView):
    template_name = 'registration.html'
    form_class = RegistrationForm
    success_url = '/thanks/'

    def form_valid(self, form):
        f1 = form.cleaned_data['firstname']
        f3 = form.cleaned_data['username']
        f4 = form.cleaned_data['password']
        Client.objects.create(first_name=f1, username=f3, password=f4, email=f3)
        return super(Registration, self).form_valid(form)


class Addproduct(FormView):
    template_name = 'addproduct.html'
    form_class = AddingProductForm
    success_url = '/thanks/'

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


def thanks(request):
    return render(request, 'end.html')

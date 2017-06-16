from django.shortcuts import render
from shop.models import Client, Address, Photo, Product
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, AddingProductForm


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            f1 = form.cleaned_data['firstname']
            f2 = form.cleaned_data['lastname']
            f3 = form.cleaned_data['username']
            f4 = form.cleaned_data['password']
            f5 = form.cleaned_data['email']
            f6 = form.cleaned_data['phone']
            f7 = form.cleaned_data['address']
            f7_db, created = Address.objects.get_or_create(address=f7)
            f7_db_id = Address.objects.values('id').filter(address=f7_db)[0]['id']
            Client.objects.create(firstname=f1, lastname=f2,
                                  username=f3, password=f4,
                                  email=f5, phone=f6,
                                  addresslist=str(f7_db_id))
            return HttpResponseRedirect('/thanks/')
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})


def addproduct(request):
    if request.method == 'POST':
        form = AddingProductForm(request.POST)
        if form.is_valid():
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
            photo_list = list()

            for i in (p5, p4, p3, p2, p1):
                if i and i not in photo_list:
                    photo_list.append(i)

            photo_list_id = list()
            for i in range(0, len(photo_list)):
                f6_db, created = Photo.objects.get_or_create(filename=photo_list[i])
                f6_db_id = Photo.objects.values('id').filter(filename=f6_db)[0]['id']
                photo_list_id.append(str(f6_db_id))

            photo_str_id = ','.join(photo_list_id)
            Product.objects.create(name=f1, manufacturer=f2,
                                   price=f3, subcategory=f4,
                                   description=f5, photo=photo_str_id)
            return HttpResponseRedirect('/thanks/')
    else:
        form = AddingProductForm()

    return render(request, 'addprod.html', {'form': form})


def thanks(request):
    return render(request, 'end.html')

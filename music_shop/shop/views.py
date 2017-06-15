from django.shortcuts import render
from shop.models import Client, Address
from django.http import HttpResponseRedirect
from .forms import RegistrationForm


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
                                  addresslist=f7_db_id)
            return HttpResponseRedirect('/thanks/')
    else:
        form = RegistrationForm()

    return render(request, 'form01.html', {'form': form})


def thanks(request):
    return render(request, 'end.html')

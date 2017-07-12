from django.views.generic import ListView
from news.models import News
from main.mixins import CategoryViewMixin
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect
from .models import Product
from categories.models import SubCategory


class Cart(ListView, CategoryViewMixin):
    template_name = 'cart.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(Cart, self).get_context_data(**kwargs)
        if 'cart' in self.request.session:
            context['cart'] = []
            for i in list(dict.fromkeys(self.request.session['cart'].keys())):
                item = {}
                item['id'] = i
                item['subcatalog'] = Product.objects.values('subcategory_id').filter(id=i)[0]['subcategory_id']
                item['catalog'] = SubCategory.objects.values('category_id').filter(id=item['subcatalog'])[0]['category_id']
                item['itemquant'] = self.request.session['cart'][i]
                item['itemname'] = Product.objects.values('name').filter(id=i)[0]['name']
                item['itemprice'] = Product.objects.values('price').filter(id=i)[0]['price']
                item['itogo'] = item['itemprice'] * item['itemquant']
                context['cart'].append(item)
            summa= 0
            for i in context['cart']:
                summa = summa + i['itogo']
            context['cart_itogo'] = summa
        return context


class AddtoCart(RedirectView):
    '''
        Создает корзину пользователя request.session['cart'] и запоминает
        в ней добавленные товары и их количество (пока по кол-ву кликов).
        Также потом позволяет изменять их количество.
    '''
    def dispatch(self, request, itemid='0', itemquantity='0', *args, **kwargs):
        if 'cart' in request.session:
            if itemid in request.session['cart']:
                if request.session['cart'][itemid] + int(itemquantity) < 0:
                    request.session['cart'][itemid] = 0
                else:
                    request.session['cart'][itemid] += int(itemquantity)
            else:
                request.session['cart'][itemid] = int(itemquantity)
        else:
            request.session['cart'] = {}
            request.session['cart'][itemid] = int(itemquantity)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DelFromCart(RedirectView):

    def dispatch(self, request, itemid='0', *args, **kwargs):
        if 'cart' in request.session:
            request.session['cart'].pop(itemid)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from categories.models import Category
from .models import Profile
from orders.models import Order, OrderItem
from main.mixins import CategoryViewMixin


class Registration(FormView, CategoryViewMixin):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        form.cleaned_data['email'] = form.cleaned_data['username']
        new_user = User.objects.create_user(**form.cleaned_data)
        login(self.request, new_user)
        return super(Registration, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Registration, self).get_context_data(**kwargs)
        return context


class LoginFormView(FormView, CategoryViewMixin):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LoginFormView, self).get_context_data(**kwargs)
        return context


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class ProfileView(DetailView, CategoryViewMixin):
    template_name = 'profile.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['orderlist'] = Order.objects.filter(user=context['profile'])
        context['orderitems'] = OrderItem.objects.filter(order__user=context['profile'])
        return context

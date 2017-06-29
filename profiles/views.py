from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import FormView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

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
    form_class = LoginForm
    template_name = 'login.html'
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
    return render(request, 'success.html')

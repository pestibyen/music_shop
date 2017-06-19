from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^addproduct/$', views.Addproduct.as_view(), name='addproduct'),
    url(r'^registration/$', views.Registration.as_view(), name='registration'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^success/$', views.success, name='success'),
]

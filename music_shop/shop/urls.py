from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^registration/$', views.Registration.as_view(), name='registration'),
    url(r'^addproduct/$', views.Addproduct.as_view(), name='addproduct'),
    url(r'^thanks/', views.thanks),
]

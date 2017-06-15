from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.registration),
    url(r'^registration/', views.registration),
    url(r'^thanks/', views.thanks),
]

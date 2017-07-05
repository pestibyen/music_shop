from django.conf.urls import url
from .views import Registration, LoginFormView, LogoutView, ProfileView

urlpatterns = [
    url(r'^registration/$', Registration.as_view(), name='registration'),
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^profile/(?P<pk>\d+)$', ProfileView.as_view(), name='profile'),
]

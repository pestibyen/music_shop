from django.conf.urls import url
from .views import IndexView
from categories.views import CatalogView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/', IndexView.as_view(template_name="about.html"), name='about'),
    url(r'^contacts/', IndexView.as_view(template_name="contacts.html"), name='contacts'),
    url(r'^catalog(?P<catid>\d)/$', CatalogView.as_view(), name='catalogs'),
]

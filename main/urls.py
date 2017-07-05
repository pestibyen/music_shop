from django.conf.urls import url
from .views import IndexView
from categories.views import CatalogView, SubCatalogView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/', IndexView.as_view(template_name="about.html"), name='about'),
    url(r'^contacts/', IndexView.as_view(template_name="contacts.html"), name='contacts'),
    url(r'^catalog(?P<catid>\d)/$', CatalogView.as_view(), name='catalogs'),
    url(r'^subcatalog(?P<catid>\d)(?P<subcatid>[0-9]+)/$', SubCatalogView.as_view(), name='subcatalogs'),
]

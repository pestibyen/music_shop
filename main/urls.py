from django.conf.urls import url
from .views import IndexView
from categories.views import CatalogView, SubCatalogView
from products.views import ProductView
from orders.views import Cart, AddtoCart, DelFromCart

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/$', IndexView.as_view(template_name="about.html"), name='about'),
    url(r'^contacts/$', IndexView.as_view(template_name="contacts.html"), name='contacts'),
    url(r'^catalog/(?P<catid>\d)/$', CatalogView.as_view(), name='catalogs'),
    url(r'^subcatalog/(?P<catid>\d)/(?P<subcatid>[0-9]+)/$', SubCatalogView.as_view(), name='subcatalogs'),
    url(r'^item/(?P<catid>\d)/(?P<subcatid>[0-9]+)/(?P<itemid>[0-9]+)/$', ProductView.as_view(), name='items'),
    url(r'^cart/$', Cart.as_view(), name='cart'),
    url(r'^addtocart/(?P<itemid>[0-9]+)/(?P<itemquantity>[0-9]+)/$', AddtoCart.as_view(), name='addtocart'),
    url(r'^minus/(?P<itemid>[0-9]+)/(?P<itemquantity>[-0-9]+)/$', AddtoCart.as_view(), name='minus'),
    url(r'^plus/(?P<itemid>[0-9]+)/(?P<itemquantity>[0-9]+)/$', AddtoCart.as_view(), name='plus'),
    url(r'^del/(?P<itemid>[0-9]+)/$', DelFromCart.as_view(), name='del'),
]

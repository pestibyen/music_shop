from django.conf.urls import url
from .views import Addproduct, success

urlpatterns = [
    url(r'^addproduct/$', Addproduct.as_view(), name='addproduct'),
    url(r'^success/$', success, name='success'),
]

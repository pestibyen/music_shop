from django.conf.urls import url
from .views import Addproduct

urlpatterns = [
    url(r'^addproduct/$', Addproduct.as_view(), name='addproduct'),
]

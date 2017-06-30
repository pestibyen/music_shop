from django.conf.urls import url
from .views import NewsViewList

urlpatterns = [
    url(r'^news/$', NewsViewList.as_view(), name='news'),
]

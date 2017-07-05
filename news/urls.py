from django.conf.urls import url
from .views import NewsViewList, NewsDetailView

urlpatterns = [
    url(r'^news/(?P<pk>\d+)$', NewsDetailView.as_view(), name='news_detail'),
    url(r'^news/$', NewsViewList.as_view(), name='news'),
]

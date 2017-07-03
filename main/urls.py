from django.conf.urls import url
from .views import IndexView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^about/', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^contacts/', TemplateView.as_view(template_name="contacts.html"), name='contacts'),
]

from django.views.generic import ListView
from news.models import News
from categories.models import Category, SubCategory
from main.mixins import CategoryViewMixin


class IndexView(ListView, CategoryViewMixin):
    template_name = 'index.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['subcatalogs'] = SubCategory.objects.values('id', 'name')
        return context

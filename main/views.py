from django.views.generic import ListView
from news.models import News
from categories.models import Category, SubCategory


class IndexView(ListView):
    template_name = 'index.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['catalogs'] = Category.objects.values('id', 'name')
        context['subcatalogs'] = SubCategory.objects.values('id', 'name')
        return context

from django.views.generic.base import ContextMixin
from categories.models import Category


class CategoryViewMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoryViewMixin, self).get_context_data(**kwargs)
        context['catalogs'] = Category.objects.values('id', 'name')
        return context

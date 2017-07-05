from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News
from categories.models import Category


class NewsViewList(ListView):
    template_name = 'news_list.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsViewList, self).get_context_data(**kwargs)
        context['catalogs'] = Category.objects.values('id', 'name')
        return context


class NewsDetailView(DetailView):
    template_name = 'news_detail.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        return context

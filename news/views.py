from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News


class NewsViewList(ListView):
    template_name = 'news_list.html'
    model = News

    def get_context_data(self, **kwargs):
        context = super(NewsViewList, self).get_context_data(**kwargs)
        return context

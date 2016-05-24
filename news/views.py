from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from .models import News


class IndexView(ListView):
    model = News
    template_name = 'news_list.html'
    paginate_by = 30

    def get_queryset(self):
        return News.objects.filter(is_active=True)


class DetailNews(DetailView):
    model = News
    template_name = 'news_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(News, slug=self.kwargs['slug'])

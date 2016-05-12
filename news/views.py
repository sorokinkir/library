from django.views.generic import ListView
from .models import News


class IndexView(ListView):
    model = News
    template_name = 'news_list.html'

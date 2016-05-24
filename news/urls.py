from django.conf.urls import url
from .views import IndexView, DetailNews


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[\w-]+)/$', DetailNews.as_view(), name='news-detail'),
]

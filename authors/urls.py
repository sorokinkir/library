from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.AuthorsView.as_view(), name='authors-index'),
    url(r'^(?P<slug>[\w-]+)/$', views.AuthorsDetail.as_view(), name='author-detail'),
]

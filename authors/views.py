from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, View
from django.db.models import Q

from .models import Authors


class AuthorsView(ListView):
    """Вывод всех авторов из бд"""
    model = Authors
    template_name = 'authors_list.html'
    paginate_by = 30


class AuthorsDetail(DetailView):
    """Вывод детальной информации по автору"""
    model = Authors
    template_name = 'authors_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Authors, slug=self.kwargs['slug'])


class Search(View):
    """Поиск всех авторов запросом вида /search/?q=<query> URL"""
    def get(self, request, q):
        query = self.request.GET.get('q')
        print(query)
        if query:
            search = Q(Authors.objects.filter(name__icontains=query)) | \
                     Q(Authors.objects.filter(surname__icontains=query))
            return JsonResponse(search, safe=False)
        else:
            return render(request, 'search.html', {})

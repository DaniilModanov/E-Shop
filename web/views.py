from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from web.models import GoodCard
from web.filters import GoodFilter


def index(request):
    return render(request, "web/home.html")


class GoodListView(ListView):
    model = GoodCard
    paginate_by = 5
    template_name = "web/home.html"
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        context['filter'] = GoodFilter(self.request.GET, queryset=queryset)

        return context

    def get_queryset(self):
        queryset = GoodCard.objects.all()
        return GoodFilter(self.request.GET, queryset=queryset).qs

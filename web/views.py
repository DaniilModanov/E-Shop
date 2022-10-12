from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from web.models import GoodCard
from web.filters import GoodFilter
from web.utils import get_choices


def index(request):
    return render(request, "web/home.html")


class GoodListView(ListView):
    model = GoodCard
    paginate_by = 6
    template_name = "web/home.html"
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        choices = get_choices()
        context['filter'] = GoodFilter(self.request.GET, queryset=queryset, choices=choices)

        return context

    def get_queryset(self):
        queryset = GoodCard.objects.all()
        choices = get_choices()
        return GoodFilter(self.request.GET, queryset=queryset, choices=choices).qs

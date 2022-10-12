from django_filters import FilterSet, CharFilter


class GoodFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')

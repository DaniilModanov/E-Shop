from django.shortcuts import get_object_or_404
from django_filters import FilterSet, CharFilter, ChoiceFilter
from web.models import GoodCard, GoodCategory
from web.utils import get_choices, CHOICES_FOR_CATEGORY_FILTER


class GoodFilter(FilterSet):

    def filter_by_category(self, queryset, name, value):

        if value != '':
            category = get_object_or_404(GoodCategory, title=value)
            return GoodCard.objects.filter(category=category)
        else:

            return GoodCard.objects.all()

    category = ChoiceFilter(method='filter_by_category', empty_label='Any furniture')
    title = CharFilter(lookup_expr='icontains')

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')

        super(GoodFilter, self).__init__(*args, **kwargs)
        CHOICES_FOR_CATEGORY_FILTER = choices
        self.filters['category'].extra.update(
            {
                'choices': CHOICES_FOR_CATEGORY_FILTER
            }
        )

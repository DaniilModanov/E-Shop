from web.models import GoodCategory

CHOICES_FOR_CATEGORY_FILTER = [
    ('', 'Any'),
]


def get_choices():
    query = GoodCategory.objects.order_by().values_list('title').distinct()
    choices = []
    for choice in query:
        temp = (choice[0], choice[0].capitalize())
        choices.append(temp)
    return choices

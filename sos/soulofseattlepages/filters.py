import django_filters
from .models import userPost

class filterPost(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

def filter_by_order(self, queryset, name, value):
    expression = 'post_CreatedOn' if value == 'ascending' else '-post_CreatedOn'
    return queryset.order_by(expression)
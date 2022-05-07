import django_filters
from dashboard.models import *


class SalesFilter(django_filters.FilterSet):
    class Meta:
        model = Sales
        fields = {
            'year': ['lte', 'gte'],
            'month': ['exact'],
            'sales': ['lte', 'gte'],

        }


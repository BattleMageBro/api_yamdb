import django_filters.rest_framework
from django_filters import filters
from .models import Titles


class TitlesFilter(django_filters.rest_framework.FilterSet):
    genre = filters.CharFilter(field_name="genre")
    category = filters.CharFilter(field_name="category")   
    year = filters.NumberFilter(field_name='year')
    name = filters.CharFilter(field_name='name', lookup_expr='contains') 

    class Meta:
        model = Titles
        fields = ['genre', 'category', 'year', 'name']
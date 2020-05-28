from django.shortcuts import render
from rest_framework import viewsets, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Categories, Genres, Titles
from . import serializers




class CategoriesViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin, 
                        viewsets.GenericViewSet):
    queryset = Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    lookup_field = 'slug'

    

class GenresViewSet(mixins.ListModelMixin, 
                    mixins.CreateModelMixin, 
                    mixins.DestroyModelMixin, 
                    viewsets.GenericViewSet):
    queryset = Genres.objects.all()
    serializer_class = serializers.GenresSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    lookup_field = 'slug'


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    filters_backends = [DjangoFilterBackend]
    filters_fields = ['genre', 'category', 'year', 'name',]
    lookup_field = 'id'

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ListTitlesSerializer
        return serializers.TitlesSerializer





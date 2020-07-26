from django.shortcuts import render
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import AllowAny
from api_users.permissions import IsAdministrator
from django_filters.rest_framework import DjangoFilterBackend
from .models import Categories, Genres, Titles
from . import serializers
from .filters import TitlesFilter




class CategoriesViewSet(mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin, 
                        viewsets.GenericViewSet):
    queryset = Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    lookup_field = 'slug'
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAdministrator],
                                    'destroy': [IsAdministrator]
                                    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            return [permission() for permission in self.permission_classes]

    

class GenresViewSet(mixins.ListModelMixin, 
                    mixins.CreateModelMixin, 
                    mixins.DestroyModelMixin, 
                    viewsets.GenericViewSet):
    queryset = Genres.objects.all()
    serializer_class = serializers.GenresSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]
    lookup_field = 'slug'
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAdministrator],
                                    'destroy': [IsAdministrator]
                                    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            return [permission() for permission in self.permission_classes]


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitlesFilter
    lookup_field = 'id'
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsAdministrator],
                                    'partial_update' : [IsAdministrator],
                                    'retrieve': [AllowAny],
                                    'destroy': [IsAdministrator]
                                    }



    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ListTitlesSerializer
        if self.action == 'retrieve':
            return serializers.ListTitlesSerializer
        return serializers.TitlesSerializer
        

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            return [permission() for permission in self.permission_classes_by_action[self.action]]

    





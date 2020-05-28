from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoriesViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
    path('categories/<slug:slug>/', views.CategoriesViewSet.as_view(actions={'delete': 'destroy'})),
    path('genres/', views.GenresViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
    path('genres/<slug:slug>/', views.GenresViewSet.as_view(actions={'delete': 'destroy'})),
    path('titles/', views.TitlesViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
    path('titles/<int:id>/', views.TitlesViewSet.as_view(actions={'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'})),
]
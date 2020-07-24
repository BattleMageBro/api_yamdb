from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import CommentViewsSet, ReviewViewsSet

router = DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewsSet)
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewsSet)

urlpatterns = [
    path('', include(router.urls)), 
]
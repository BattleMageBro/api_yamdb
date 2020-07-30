from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import CommentViewsSet, ReviewViewsSet

router = DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewsSet, basename='review')                
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewsSet, 
    basename='comment'
)

urlpatterns = [
    path('api/v1/', include(router.urls)), 
]
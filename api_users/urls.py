from django.urls import include, path 
from rest_framework.authtoken import views 
from rest_framework.routers import DefaultRouter
from api_users import views
from .views import UsersViewSet
 
router = DefaultRouter() 

router.register('users', UsersViewSet, basename='users') 
#router.register('auth/token/', views.get_token) 

urlpatterns = [ 
    path('', include(router.urls)),
    path('auth/email/', views.send_confirmation_code),
    path('auth/token/', views.get_token)
]
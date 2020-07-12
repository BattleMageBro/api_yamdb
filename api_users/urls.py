from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api_users import views

from .views import UserViewSet

router = DefaultRouter()  
router.register(r'users', UserViewSet, basename='users') 

urlpatterns = [ 
    path('auth/email/', views.send_confirmation_code),
    path('auth/token/', views.get_token), 
]

urlpatterns += [
    path('v1/', include(router.urls)),
]

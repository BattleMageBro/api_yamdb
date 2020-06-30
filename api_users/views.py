from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from .serializers import EmailSerializer, EmailCodeSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import filters, status, viewsets
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from django.shortcuts import get_object_or_404
from .permissions import IsAdministrator

@api_view(['POST'])
def send_confirmation_code(request):
    serializer = EmailSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data['email']
        if not User.objects.filter(email=email):
            Member=User.objects.create_user(email=email)
        else:
            Member=User.objects.get(email=email) 
        confirmation_code = PasswordResetTokenGenerator().make_token(Member)
        send_mail(
        'Confirmation code',
        confirmation_code,
        'yamdb@example.com',
        [email],
        fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def get_token(request):
    serializer = EmailCodeSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.data['email']
        code = serializer.data['code']
        Member=User.objects.get(email=email)
        if PasswordResetTokenGenerator().check_token(Member, code):
            token = AccessToken.for_user(Member)
            return Response({'token': f'{token}'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'username'
    permission_classes = [IsAdministrator,]


class APIUser(APIView):

    def get(self, request):
        user = get_object_or_404(User, username=self.request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request):
        user = get_object_or_404(User, username=self.request.user)
        serializer = UserSerializer(user,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

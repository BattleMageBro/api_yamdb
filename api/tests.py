from rest_framework.viewsets import ModelViewSet

from django.test import TestCase

from .models import Comment, Review, Title
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewsSet(ModelViewSet):
    queryset = Review.objects.all()
    

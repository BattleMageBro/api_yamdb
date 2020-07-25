from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.db.models import Avg
from django.shortcuts import get_object_or_404

from .models import Comment, Review, Titles
from .permissions import IsAuthor, IsModerator
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewsSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAuthor, IsModerator,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        title = get_object_or_404(Titles, pk=self.request.kwargs.get('title_id', None))
        serializer.save(author=self.request.user, title=title)
        
        reviews = title.reviews.all()
        if reviews.count() > 0:
            title.rating = reviews.aggregate(Avg('score')).get('score__avg', None)
            title.save() 


class CommentViewsSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthor, IsModerator,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  

from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.db.models import Avg
from django.shortcuts import get_object_or_404

from titles.models import Titles
from .models import Comment, Review
from .permissions import IsAuthorOrStaff
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewsSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAuthorOrStaff,
        IsAuthenticatedOrReadOnly
    )

    def set_rating(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles,pk=title_id)
        reviews = Review.objects.filter(title=title)
        rating = reviews.aggregate(Avg('score')).get('score__avg')
        title.rating = rating
        title.save()

    def perform_destroy(self, instance):
        instance.delete()
        self.set_rating()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles, pk=title_id)
        serializer.save(author=self.request.user, title=title)
        self.set_rating()
    
    def perform_update(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles, pk=title_id)
        serializer.save(author=self.request.user, title=title)
        self.set_rating()

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Titles, pk=title_id)
        return Review.objects.filter(title=title)



class CommentViewsSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthorOrStaff,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id)
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id)
        comments = Comment.objects.filter(review=review)
        return comments

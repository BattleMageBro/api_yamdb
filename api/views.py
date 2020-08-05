from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.db.models import Avg
from django.shortcuts import get_object_or_404

from titles.models import Titles
from .models import Comment, Review
from .permissions import IsAuthorOrStaff
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewsSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAuthorOrStaff,
        IsAuthenticatedOrReadOnly
    )

    def get_title(self):
        return get_object_or_404(Titles, pk=self.kwargs.get('title_id'))

    def set_rating(self):
        title = self.get_title()
        reviews = title.reviews.all()
        rating = reviews.aggregate(Avg('score')).get('score__avg')
        title.rating = rating
        title.save()

    def perform_destroy(self, instance):
        instance.delete()
        self.set_rating()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())
        self.set_rating()

    def perform_update(self, serializer):
        serializer.save(author=self.request.user, title=self.get_title())
        self.set_rating()

    def get_queryset(self):
        title = self.get_title()
        return title.reviews.all()


class CommentViewsSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthorOrStaff,
        IsAuthenticatedOrReadOnly
    )

    def get_review(self):
        return get_object_or_404(Review, pk=self.kwargs.get('review_id'))

    def perform_create(self, serializer):
        review = self.get_review()
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = self.get_review()
        return review.comments.all()

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.db.models import Avg
from django.shortcuts import get_list_or_404, get_object_or_404

from titles.models import Titles
from .models import Comment, Review
from .permissions import IsAuthor, IsModerator
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewsSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        IsAuthor, IsModerator,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        title = Titles.objects.get(pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
        reviews = Review.objects.filter(title=title)
        title.rating = reviews.aggregate(Avg('score')).get('score__avg')
        title.save()

    


class CommentViewsSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsAuthor, IsModerator,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        review = get_object_or_404(Review,pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)

    
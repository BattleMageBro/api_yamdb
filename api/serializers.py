from rest_framework.serializers import (
    CharField, IntegerField, ModelSerializer,
    ValidationError
)

from .models import Comment, Review


def score_limits(value):
    if not 1 <= value <= 10:
        raise ValidationError('Bad request')


class CommentSerializer(ModelSerializer):
    author = CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'pub_date']
        read_only_fields = ['id', 'pub_date', ]


class ReviewSerializer(ModelSerializer):
    author = CharField(source='author.username', read_only=True)
    score = IntegerField(validators=[score_limits])

    class Meta:
        model = Review
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        read_only_fields = ['id', 'score', 'pub_date']

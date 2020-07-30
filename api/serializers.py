from rest_framework.serializers import (
    CharField, IntegerField, ModelSerializer,
    ValidationError
)

from .models import Comment, Review

from titles.models import Titles

def score_limits(value):
    if not 1 <= value <= 10:
        raise ValidationError('Bad request')


def score_limits(value):
    if not 1 <= value <= 10:
        raise ValidationError('Bad request')


class CommentSerializer(ModelSerializer):
    author = CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'pub_date']
        read_only_fields = ['id', 'pub_date']


class ReviewSerializer(ModelSerializer):
    author = CharField(source='author.username', read_only=True)
    score = IntegerField(validators=[score_limits])

    class Meta:
        model = Review
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        read_only_fields = ['id', 'score', 'pub_date']

    def validate(self, data):
        title_id = self.context.get('view').kwargs.get('title_id')
        user = self.context.get('request').user
        
        if self.context.get('request').method == 'POST':
            if (not Titles.objects.filter(id=title_id).exists()) or not bool(data):
                return ValidationError

            if Review.objects.filter(author=user, title__id=title_id).exists():
                raise ValidationError
        return data

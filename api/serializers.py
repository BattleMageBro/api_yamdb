from rest_framework.serializers import CharField, ModelSerializer

from .models import Comment, Review


class CommentSerializer(ModelSerializer):
    author = CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'pub_date']
        read_only_fields = ['pub_date', ]


class ReviewSerializer(ModelSerializer):
    author = CharField(source='author.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        read_only_fields = ['score', 'pub_date']

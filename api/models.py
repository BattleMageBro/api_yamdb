from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Review(models.Model):
    title = models.ForeignKey(
        'titles.Titles', on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')

    text = models.TextField()
    score = models.PositiveSmallIntegerField(default=1)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reviews'


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
        
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'

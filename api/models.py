from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Title(models.Model):
    rating = models.FloatField(default=0)


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    score = models.SmallIntegerField(
        default=1, 
        choices=[(value, value) for value in range(1, 11, 1)]
    )
    pub_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='commets')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commets')
    pub_date = models.DateTimeField(auto_now_add=True)

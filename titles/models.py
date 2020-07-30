from django.db import models



class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, primary_key=True)


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, primary_key=True)


class Titles(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    genre = models.ManyToManyField(Genres, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.FloatField(default=None, blank=True, null=True)

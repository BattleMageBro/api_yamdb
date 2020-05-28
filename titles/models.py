from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


class Titles(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    genre = models.ManyToManyField(Genres, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, blank=True, null=True)
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=50, null=True, unique=True)

    def __str__(self):
        return self.country_name


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age_limit = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    full_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.full_name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(
        null=True, validators=[MaxValueValidator(10), MinValueValidator(1)]
    )
    released = models.DateField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.DO_NOTHING)
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)
    countries = models.ManyToManyField(Country, related_name='movies')

    def __str__(self):
        return f"{self.title} from {self.released}"

    class Meta:
        unique_together = ('title', 'released')

#
# #1.
# Movie.objects.filter(countries__name__in=['Poland', 'Germany']).distinct()
# #2.
# Movie.objects.filter(released__year__gt=2020, rating__gte=8)
# #3.
# from django.db.models import Count
# genres = Movie.objects.values('genre').annotate(genres_count=Count('genre')).filter(genres_count__gte=2).values_list('genre')Movie.objects.filter(genre__in=genres)




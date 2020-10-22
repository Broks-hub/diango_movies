from django.contrib import admin

from core.models import Movie
from core.models import Genre

admin.site.register(Movie)
admin.site.register(Genre)

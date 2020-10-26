from django.contrib import admin

from core.models import Movie
from core.models import Genre
from core.models import Director

from core.models import Country

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Country)


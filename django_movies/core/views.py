from django.shortcuts import render
from django import views
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse

from core.models import Movie, AGE_LIMIT


class MovieView(ListView):
    template_name = 'movies.html'
    model = Movie

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['limits'] = AGE_LIMIT
        return result


def movies(request):
    return render(
        request,
        template_name='movies.html',
        context={'movies': Movie.objects.all(),
                 'limits': AGE_LIMIT}
        # context={'movies': Movie.objects.exclude(genre__age_limit=AGE_LIMIT.adult)},
    )


def hello(request):
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': ['beatufiul', 'cruel', 'wonderfull']}
    )

# def hello(request):
#     return HttpResponse('Hello world!')


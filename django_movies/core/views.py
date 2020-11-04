from django.shortcuts import render
from django import views
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, DeleteView, UpdateView, DetailView
from django.http import HttpResponse

from core.models import Movie, AGE_LIMIT

from core.forms import MovieForm
from pip._internal.utils import logging


# logging.basicConfig()


class MovieUpdateView(UpdateView):
    template_name = 'core/form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('index')


class MovieCreateView(CreateView):
    title = 'Add Movie'
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movie_create')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

    # def form_valid(self, forms):
    #     forms.save()
    #     return super().form_valid(forms)


class MovieListView(ListView):
    template_name = 'movies.html'
    model = Movie

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['limits'] = AGE_LIMIT
        return result


class IndexView(MovieListView):
    template_name = 'index.html'


class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie


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

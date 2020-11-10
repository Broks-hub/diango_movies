from core.views import MovieListView


class IndexView(MovieListView):
    title = 'Welcome'
    template_name = 'index.html'

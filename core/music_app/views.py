from django.views.generic import ListView

from . models import Song

class SongView(ListView):
    paginate_by = 2
    model = Song
    template_name = 'index.html'
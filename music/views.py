from django.views import generic
from .models import Album


class IndexView(generic.ListView):
    template_name =

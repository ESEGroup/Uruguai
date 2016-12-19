from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

class IndexView(RedirectView):

    permanent = False
    url = reverse_lazy('inspection_list')

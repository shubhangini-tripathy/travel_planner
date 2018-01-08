from django.views.generic import ListView
from .models import Travel


class HomePageView(ListView):
    model = Travel
    template_name = 'travel.html'
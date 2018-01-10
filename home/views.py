from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Travel


class HomePageView(ListView):
    model = Travel
    template_name = 'travel.html'


class TravelDetailView(DetailView):
    model = Travel
    template_name = 'travel_detail.html'


class TravelCreateView(CreateView):
    model = Travel
    template_name = 'travel_new.html'
    fields = '__all__'

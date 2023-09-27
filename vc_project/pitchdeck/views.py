from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PitchDeck


class PitchDeckView(CreateView):
    """ A view to upload pitches """

    model = PitchDeck
    fields = ['name', 'company_name',  'Sector', 'Location', 'PMV', 'Raising', 'Email', 'Assurance', 'Stage', 'upload',]
    template_name = 'pitchdeck/pitchdeck.html'
    success_url = reverse_lazy('portfolio')


class PitchDeckListView(ListView):
    """ A View to render a list of pitches """

    model = PitchDeck
    template_name = 'pitchdeck/pitchdeck_list_view.html'
    context_object_name = 'pitchdeck'

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.db import models
from django.views.generic import ListView, CreateView, UpdateView

from .models import Home

class Index(ListView):
    """A view to return the index page"""
    model = Home
    template_name = 'home/index.html'
    context_object_name = 'home'
    success_url = reverse_lazy('home')


class EditHomePageView(UpdateView):
    model = Home
    template_name = 'home/edit_home_page.html'
    fields = ['title', 'content', 'icon']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('home')
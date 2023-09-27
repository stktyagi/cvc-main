from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PortfolioForm
from .models import Portfolio

class PortfolioListView(ListView):
    """ A View to render a list of portfolio items """


    model = Portfolio
    template_name = 'portfolio/portfolio_list_view.html'
    context_object_name = 'portfolio'

class AddPorfolioItemView(CreateView):
    """ A view to add new items to the portfolio """

    
    model = Portfolio
    fields = ['title', 'link', 'image']
    template_name = 'portfolio/add_portfolio_item.html'
    success_url = reverse_lazy('portfolio')


class EditPortfolioItemView(UpdateView):
    model = Portfolio
    template_name = 'portfolio/edit_portfolio_item.html'
    fields = ['title', 'link', 'image']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('portfolio')


class DeletePortfolioItemView(DeleteView):
    model = Portfolio
    template_name = 'portfolio/delete_portfolio_item.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('portfolio')
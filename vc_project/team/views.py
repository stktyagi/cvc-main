from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Team

class TeamListView(ListView):
    """ A View to render a list of portfolio items """

    model = Team
    template_name = 'team/team_list_view.html'
    context_object_name = 'team'


class AddTeamMemberView(CreateView):
    """ A view to add new items to the portfolio """
    
    model = Team
    fields = ['name', 'title', 'description', 'country', 'linkedin', 'image']
    template_name = 'team/add_team_member.html'
    success_url = reverse_lazy('team')


class EditTeamMemberView(UpdateView):
    model = Team
    template_name = 'team/edit_team_member.html'
    fields = ['name', 'title', 'description', 'country', 'linkedin', 'image']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('team')

class DeleteTeamMemberView(DeleteView):
    model = Team
    template_name = 'team/delete_team_member.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('team')
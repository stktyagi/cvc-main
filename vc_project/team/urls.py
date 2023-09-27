from django.urls import path
from .views import TeamListView, AddTeamMemberView, EditTeamMemberView, DeleteTeamMemberView
from . import views


urlpatterns = [
    path('', TeamListView.as_view(), name='team'),
    path('add_team_member/', AddTeamMemberView.as_view(), name='add_team_member'),
    path('<int:pk>/edit/', EditTeamMemberView.as_view(), name='edit_team_member'),
    path('delete/<int:pk>', DeleteTeamMemberView.as_view(), name='delete_team_member'),

]
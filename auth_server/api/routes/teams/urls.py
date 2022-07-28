from django.urls import path
from auth_server.api.views.teams.index import getTeams, addTeam

urlpatterns = [
    path('list', getTeams, name='delete-user'),
    path('create', addTeam, name='update-user')
]
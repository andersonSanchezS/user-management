from django.db import models
# Models
from django.contrib.auth.models import User
from auth_server.api.models.teams.index import Team


class TeamMember(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    teamId = models.ForeignKey(Team, on_delete=models.CASCADE)
    state = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return str(self.description)

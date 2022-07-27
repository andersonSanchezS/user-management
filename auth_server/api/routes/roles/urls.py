from django.urls import path
from auth_server.api.views.roles.index import roleList

urlpatterns = [
    path('list/', roleList, name='role-list')
]
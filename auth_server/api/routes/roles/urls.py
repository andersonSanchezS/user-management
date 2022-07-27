from django.urls import path
from auth_server.api.views.roles.index import roleList, addRole, remove_role

urlpatterns = [
    path('list/', roleList, name='role-list'),
    path('add/<int:pk>', addRole, name='role-add'),
    path('remove/<int:pk>', remove_role, name='role-remove')
]
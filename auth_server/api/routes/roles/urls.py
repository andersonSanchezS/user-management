from django.urls import path
from auth_server.api.views.roles.index import roleList, addRole, removeRole

urlpatterns = [
    path('list/', roleList, name='role-list'),
    path('add/<int:pk>', addRole, name='role-add'),
    path('remove/<int:pk>', removeRole, name='role-remove')
]
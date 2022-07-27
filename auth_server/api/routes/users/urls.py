from django.urls import path
from auth_server.api.views.users.index import deleteUser, updateUser

urlpatterns = [
    path('delete/<int:pk>', deleteUser, name='delete-user'),
    path('update/<int:pk>', updateUser, name='update-user')
]
from django.urls import path, include

urlpatterns = [
    path('auth/', include('auth_server.api.routes.users.urls')),
    path('roles/', include('auth_server.api.routes.roles.urls')),
]
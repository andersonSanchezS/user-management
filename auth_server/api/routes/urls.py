from django.urls import path, include

urlpatterns = [
    path('auth/', include('auth_server.api.routes.auth.urls')),
    path('roles/', include('auth_server.api.routes.roles.urls')),
    path('users/', include('auth_server.api.routes.users.urls')),
]
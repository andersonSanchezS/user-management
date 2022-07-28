from django.urls import path, include
from auth_server.api.views.users.index import registerUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from auth_server.api.views.auth.index import MyTokenObtainPairView

urlpatterns = [
    path('register/', registerUser, name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
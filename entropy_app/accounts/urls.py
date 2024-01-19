from django.urls import path
from accounts.views import CreateUser, UserLogin

urlpatterns = [
    path('signup/', CreateUser.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
]
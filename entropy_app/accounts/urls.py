from django.urls import path
from accounts.views import CreateUser

urlpatterns = [
    path('signup/', CreateUser.as_view(), name='signup')
]
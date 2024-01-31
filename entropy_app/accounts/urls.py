"""
    Module name :- urls
"""

from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import (
    CreateUser,
    UserLogin,
    ListUser,
    DeleteUser,
    UpdateUser,
    SearchUser,
)

app_name = "accounts"

urlpatterns = [
    path("signup/", CreateUser.as_view(), name="signup"),
    path("login/", UserLogin.as_view(), name="login"),
    path("profiles/", ListUser.as_view(), name="profiles"),
    path("update-user/<int:pk>/", UpdateUser.as_view(), name="update-user"),
    path("delete-user/<int:pk>/", DeleteUser.as_view(), name="delete-user"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("search/user/", SearchUser.as_view(), name="user_search"),
]

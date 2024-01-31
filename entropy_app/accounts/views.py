"""
    Module name :- views
"""

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from accounts.forms import UserForm, UserAuthenticationForm, UpdateUserForm


# Create your views here.
@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class CreateUser(SuccessMessageMixin, PermissionRequiredMixin, CreateView):
    """
    Create user.
    """

    model = User
    form_class = UserForm
    template_name = "accounts/signup.html"
    success_message = "User created."
    success_url = reverse_lazy("accounts:profiles")
    permission_required = "is_superuser"

    def form_invalid(self, form):
        messages.info(self.request, form.errors)
        return super().form_invalid(form)


class UserLogin(SuccessMessageMixin, LoginView):
    """
    Login form for users.
    """

    template_name = "accounts/login.html"
    form_class = UserAuthenticationForm
    success_message = "Login Successful."

    def form_valid(self, form):
        response = super().form_valid(form)
        next_url = self.request.GET.get("next", None)

        return redirect(next_url) if next_url else response

    def get_success_url(self) -> str:
        return reverse_lazy("inventory:nomenclatures")


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class ListUser(ListView):
    """
    List users.
    """

    template_name = "accounts/list_user.html"
    paginate_by = 8
    model = User
    context_object_name = "users"


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class UpdateUser(SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    """
    Update user.
    """

    template_name = "accounts/update.html"
    context_object_name = "user"
    model = User
    form_class = UpdateUserForm
    success_url = reverse_lazy("accounts:profiles")
    success_message = "Profile successfully updated"

    def has_permission(self) -> bool:
        return self.request.user.is_superuser or (
            self.request.user == self.get_object()
        )


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class DeleteUser(SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    """
    Delete user.
    """

    model = User
    template_name = "accounts/delete.html"
    success_url = reverse_lazy("accounts:profiles")
    success_message = "User Deleted successfully."
    context_object_name = "user"

    def get(self, request, *args, **kwargs):
        try:
            self.get_object()
        except User.DoesNotExist:
            messages.info(request, "User does not exists.")
            return redirect("accounts:profiles")
        return super().get(request, *args, **kwargs)

    def has_permission(self) -> bool:
        return self.request.user.is_superuser or (
            self.request.user == self.get_object()
        )


class SearchUser(ListView):
    """
    Search users.
    """

    template_name = "accounts/list_user.html"
    paginate_by = 8
    context_object_name = "users"

    def get_queryset(self):
        search = self.request.GET["search"]
        return User.objects.filter(
            Q(username__icontains=search) | Q(first_name=search) | Q(last_name=search)
        )

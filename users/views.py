from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, PasswordResetView
from users.forms import (
    UserRegisterForm,
    UserProfileForm,
    UserLoginForm,
)
from users.models import User
from django.urls import reverse, reverse_lazy

from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
import secrets
from django.shortcuts import get_object_or_404, redirect
import random


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        host = self.request.get_host()
        url = f"http://{host}/users/activate/{token}"
        user.token = token
        user.save()
        send_mail(
            subject="Подтверждение регистрации",
            message=f"Для подтверждения регистрации перейдите по ссылке: {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user


class LoginUserView(LoginView):
    form_class = UserLoginForm
    template_name = "users/login.html"
    success_url = reverse_lazy("users:login")

# pyright:reportIncompatibleVarggVableOverride=false

from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from django.contrib.auth.views import PasswordResetForm
from users.models import User


class FormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class UserRegisterForm(FormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]


class UserProfileForm(FormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "avatar"]


class UserLoginForm(FormMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = [
            "email",
            "password",
        ]

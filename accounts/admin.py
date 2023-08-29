from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import forms
from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = forms.CustomUserChangeForm
    add_form = forms.CustomUserCreateForm

    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional infromation",
            {"fields": ("phone", "job", "bio")},
        ),
    )  # type: ignore

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional infromation",
            {"fields": ["phone", "job", "bio"]},
        ),
    )

    list_display = ["username", "first_name", "last_name", "email", "is_staff"]

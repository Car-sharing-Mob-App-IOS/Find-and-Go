from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, UserCoordinates


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "is_active",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
    )
    fieldsets = (
        ("Электронная почта", {"fields": ("email",)}),
        (
            _("Персональная информация"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "coordinates",
                )
            },
        ),
        (
            _("Дата"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
    ordering = ("id",)
    empty_value_display = _("Пусто")


@admin.register(UserCoordinates)
class CoordinatesCarAdmin(admin.ModelAdmin):
    list_display = [
        "latitude",
        "longitude",
    ]
    search_fields = [
        "latitude",
        "longitude",
    ]

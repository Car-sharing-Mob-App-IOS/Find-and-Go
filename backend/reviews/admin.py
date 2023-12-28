from core.texts import LIST_PER_PAGE
from django.contrib import admin

from .models import Review


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = [
        "user",
        "car",
        "score",
        "comment",
        "created_at"
        ]
    search_fields = [
        "user__mail",
    ]
    list_filter = ["score"]
    ordering = ["-created_at"]
    list_per_page = LIST_PER_PAGE

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import CoordinatesCar, Car, CarVarious


@admin.register(CarVarious)
class CarVariousAdmin(admin.ModelAdmin):
    pass


@admin.register(CoordinatesCar)
class CoordinatesCarAdmin(admin.ModelAdmin):
    list_display = [
        "latitude",
        "longitude",
    ]
    search_fields = [
        "latitude",
        "longitude",
    ]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "company",
        "brand",
        "model",
        "is_available",
        "type_car",
    ]
    search_fields = [
        "company",
        "brand",
        "model",
        "state_number",
    ]

    fieldsets = (
        (
            _("О машине"),
            {
                "fields": (
                    "image",
                    "is_available",
                    "company",
                    "brand",
                    "model",
                    "type_car",
                    "state_number",
                )
            },
        ),
        (
            _("Детали машин"),
            {
                "fields": (
                    "various",
                    "type_engine",
                    # "child_seat",
                    "power_reserve",
                    "rating",
                    "coordinates",
                ),
            },
        ),
    )


@admin.register(CarVarious)
class CarVariousAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
    ]
    search_fields = [
        "latitude",
        "longitude",
    ]
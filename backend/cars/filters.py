import django_filters
from .models import Car, CarVarious


class CarFilter(django_filters.FilterSet):
    type_car = django_filters.rest_framework.BaseInFilter()
    company = django_filters.rest_framework.BaseInFilter()
    type_engine = django_filters.rest_framework.BaseInFilter()
    child_seat = django_filters.rest_framework.BooleanFilter()
    is_available = django_filters.rest_framework.BooleanFilter()
    latitude = django_filters.rest_framework.RangeFilter(
        field_name="coordinates__latitude"
    )
    longitude = django_filters.rest_framework.RangeFilter(
        field_name="coordinates__longitude"
    )
    various = django_filters.filters.ModelMultipleChoiceFilter(
        field_name="various__slug",
        to_field_name="slug",
        queryset=CarVarious.objects.all(),
    )

    class Meta:
        model = Car
        fields = [
            "company",
            "type_car",
            "rating",
            "power_reserve",
            "child_seat",
            "type_engine",
            "model",
            "is_available",
            "latitude",
            "longitude",
            "various",
        ]

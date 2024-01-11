import django_filters

from .models import Car, CarVarious


class RatingFilter(
    django_filters.rest_framework.BaseInFilter,
    django_filters.rest_framework.NumberFilter
):
    pass


class CarFilter(django_filters.FilterSet):
    type_car = django_filters.rest_framework.BaseInFilter()
    company = django_filters.rest_framework.BaseInFilter()
    type_engine = django_filters.rest_framework.BaseInFilter()
    is_available = django_filters.rest_framework.BooleanFilter()
    power_reserve = django_filters.rest_framework.BaseInFilter()
    latitude = django_filters.rest_framework.RangeFilter(
        field_name="coordinates__latitude"
    )
    longitude = django_filters.rest_framework.RangeFilter(
        field_name="coordinates__longitude"
    )
    rating = RatingFilter()
    various = django_filters.filters.ModelMultipleChoiceFilter(
        field_name="various__slug",
        to_field_name="slug",
        queryset=CarVarious.objects.all(),
        conjoined=True
    )

    class Meta:
        model = Car
        fields = [
            "company",
            "type_car",
            "rating",
            "power_reserve",
            "type_engine",
            "model",
            "is_available",
            "latitude",
            "longitude",
            "various",
        ]

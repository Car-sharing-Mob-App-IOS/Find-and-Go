from django.db import models
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)

from core.texts import (
    CAR_BRAND_LABEL,
    CAR_CHILD_SEAT_LABEL,
    CAR_COMPANY_LABEL,
    CAR_COORDINATES_HELP_TEXT,
    CAR_COORDINATES_LABEL,
    CAR_ENGINE_TYPE_LABEL,
    CAR_HELP_TEXT_IMAGE,
    CAR_IS_AVAILABLE_LABEL,
    CAR_KIND_LABEL,
    CAR_MODEL_LABEL,
    CAR_POWER_RESERVE_LABEL,
    CAR_RATING_LABEL,
    CAR_STATE_NUMBER_LABEL,
    CAR_TYPE_LABEL,
    CAR_VERBOSE_NAME,
    CAR_VERBOSE_NAME_PLURAL,
    HELP_TEXT_LATITUDE,
    HELP_TEXT_LONGITUDE,
    CAR_KIND_CAR_CHOICES,
    CAR_NAME_COMPANY_CHOICES,
    CAR_TYPE_CAR_CHOICES,
    CAR_TYPE_ENGINE_CHOICES,
    CAR_IS_AVAILABLE_CHOICES,
    CAR_CHILD_SEAT_CHOICES,
)

from .utils import image_upload_to, resize_image
from .validators import (
    validate_state_number,
)


class CoordinatesCar(models.Model):
    """Модель, представляющая координаты местоположения."""

    latitude = models.FloatField(
        "Широта",
        validators=[
            MaxValueValidator(limit_value=90.0),
            MinValueValidator(limit_value=-90.0),
        ],
        help_text=HELP_TEXT_LATITUDE,
    )
    longitude = models.FloatField(
        "Долгота",
        validators=[
            MaxValueValidator(limit_value=180.0),
            MinValueValidator(limit_value=-180.0),
        ],
        help_text=HELP_TEXT_LONGITUDE,
    )

    class Meta:
        verbose_name = "Координата"
        verbose_name_plural = "Координаты"

    def __str__(self):
        return f"Latitude: {self.latitude}, Longitude: {self.longitude}"


class Car(models.Model):
    """Модель, представляющая информацию о автомобиле."""

    coordinates = models.OneToOneField(
        CoordinatesCar,
        verbose_name=CAR_COORDINATES_LABEL,
        help_text=CAR_COORDINATES_HELP_TEXT,
        on_delete=models.CASCADE,
        related_name="car_coordinates",
    )
    image = models.ImageField(
        upload_to=image_upload_to,
        blank=False,
        default="default_image/default_car.png",
        help_text=CAR_HELP_TEXT_IMAGE,
    )
    is_available = models.BooleanField(
        CAR_IS_AVAILABLE_LABEL,
        default=True,
        choices=CAR_IS_AVAILABLE_CHOICES,
    )
    company = models.CharField(
        CAR_COMPANY_LABEL,
        choices=CAR_NAME_COMPANY_CHOICES,
        max_length=30,
    )
    brand = models.CharField(
        CAR_BRAND_LABEL,
        max_length=30,
    )
    model = models.CharField(
        CAR_MODEL_LABEL,
        max_length=30,
    )
    type_car = models.CharField(
        CAR_TYPE_LABEL,
        choices=CAR_TYPE_CAR_CHOICES,
        max_length=30,
    )
    state_number = models.CharField(
        CAR_STATE_NUMBER_LABEL,
        max_length=10,
        validators=[validate_state_number],
    )
    type_engine = models.CharField(
        CAR_ENGINE_TYPE_LABEL,
        choices=CAR_TYPE_ENGINE_CHOICES,
        max_length=30,
    )
    child_seat = models.BooleanField(
        CAR_CHILD_SEAT_LABEL,
        default=False,
        choices=CAR_CHILD_SEAT_CHOICES,
    )
    power_reserve = models.IntegerField(CAR_POWER_RESERVE_LABEL)
    rating = models.DecimalField(
        CAR_RATING_LABEL,
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(5.00),
        ],
    )
    kind_car = models.CharField(
        CAR_KIND_LABEL,
        choices=CAR_KIND_CAR_CHOICES,
        max_length=9,
    )

    class Meta:
        verbose_name = CAR_VERBOSE_NAME
        verbose_name_plural = CAR_VERBOSE_NAME_PLURAL

    def __str__(self):
        return f"[{self.company}]: {self.brand} {self.model}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            resize_image(self.image.path)

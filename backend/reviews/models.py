from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)

from cars.models import Car
from core.texts import (
    CAR_RATING_LABEL,
    CAR_TAKEN,
    CAR_USER,
    COMMENT_CREATED_AT,
    DRIVERS_COMMENT,
    REVIEW_VERBOSE_NAME,
    REVIEW_VERBOSE_NAME_PLURAL,
)
from django.db import models
from users.models import User


class Review(models.Model):
    """Модель, представляющая отзыв об автомобиле."""

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        verbose_name=CAR_USER,
        on_delete=models.CASCADE,
    )
    car = models.ForeignKey(
        Car,
        verbose_name=CAR_TAKEN,
        on_delete=models.CASCADE,
    )
    rating = models.DecimalField(
        CAR_RATING_LABEL,
        max_digits=3,
        decimal_places=2,
        validators=[
            MinValueValidator(0.00),
            MaxValueValidator(5.00),
        ],
    )
    comment = models.TextField(DRIVERS_COMMENT, blank=True)

    created_at = models.DateTimeField(
        COMMENT_CREATED_AT,
        auto_now_add=True,
    )

    class Meta:
        verbose_name = REVIEW_VERBOSE_NAME
        verbose_name_plural = REVIEW_VERBOSE_NAME_PLURAL
        unique_together = (
            "user",
            "car",
        )

    def __str__(self):
        return (
            f"Оценка от пользователя {self.user.email} машины - "
            f"{self.car.brand} {self.car.model}"
        )

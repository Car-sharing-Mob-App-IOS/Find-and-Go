from cars.models import Car
from core.texts import (
    CAR_SCORE,
    CAR_TAKEN,
    CAR_USER, COMMENT_CREATED_AT,
    DRIVERS_COMMENT, REVIEW_VERBOSE_NAME,
    REVIEW_VERBOSE_NAME_PLURAL
    )
from django.db import models
from users.models import User


class Review(models.Model):
    """Модель, представляющая отзыв об автомобиле."""
    id = models.AutoField(primary_key=True)
    score = models.IntegerField(CAR_SCORE)
    comment = models.TextField(DRIVERS_COMMENT, blank=True)
    user = models.ForeignKey(
        User, verbose_name=CAR_USER, on_delete=models.CASCADE
        )
    car = models.ForeignKey(
        Car, verbose_name=CAR_TAKEN, on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(COMMENT_CREATED_AT, auto_now_add=True)

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

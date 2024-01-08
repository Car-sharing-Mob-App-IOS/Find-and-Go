from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import EmailValidator

from django.db import models

from core.texts import (
    DEFAULT_LENGHT,
    USER_EMAIL_VALIDATOR_MESSAGE,
    USER_HELP_TEXT_EMAIL,
    USER_HELP_TEXT_NAME,
    USER_HELP_TEXT_SURNAME,
    USER_VERBOSE_NAME,
    USER_VERBOSE_NAME_PLURAL,
    USER_RESET_CODE,
    USER_RESET_CODE_LEN,
    USER_RESET_ATTEMPTS,
    USER_COORDINATES_HELP_TEXT,
    USER_COORDINATES_LABEL,
)
from cars.models import Coordinates

from .validators import name_surname_validator


class CustomUserManager(BaseUserManager):
    """
    Менеджер модели пользователя,
    где адрес электронной почты является уникальным идентификатором
    для аутентификации, вместо имен пользователей.
    """

    def create_user(self, email, password=None, **extra_fields):
        try:
            if not email:
                raise ValueError("Поле email обязательно к заполнению.")
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)

            return user

        except Exception as e:
            raise ValueError(f"Ошибка при создании пользователя: {e}")

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Расширенная модель пользователя с дополнительными полями.
    """

    username = None
    email = models.EmailField(
        USER_HELP_TEXT_EMAIL,
        max_length=DEFAULT_LENGHT,
        unique=True,
        validators=[
            EmailValidator(message=USER_EMAIL_VALIDATOR_MESSAGE),
        ],
        help_text=USER_HELP_TEXT_EMAIL,
    )

    first_name = models.CharField(
        USER_HELP_TEXT_NAME,
        max_length=DEFAULT_LENGHT,
        validators=[
            name_surname_validator,
        ],
        help_text=USER_HELP_TEXT_NAME,
    )

    last_name = models.CharField(
        USER_HELP_TEXT_SURNAME,
        max_length=DEFAULT_LENGHT,
        validators=[
            name_surname_validator,
        ],
        help_text=USER_HELP_TEXT_SURNAME,
    )
    password_reset_code = models.CharField(
        USER_RESET_CODE,
        max_length=USER_RESET_CODE_LEN,
        blank=True,
        null=True,
    )
    password_reset_attempts = models.IntegerField(
        USER_RESET_ATTEMPTS,
        default=0,
    )
    coordinates = models.OneToOneField(
        "UserCoordinates",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="coordinates",
        verbose_name=USER_COORDINATES_LABEL,
        help_text=USER_COORDINATES_HELP_TEXT,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    class Meta:
        verbose_name = USER_VERBOSE_NAME
        verbose_name_plural = USER_VERBOSE_NAME_PLURAL

    def __str__(self) -> str:
        return self.email


class UserCoordinates(Coordinates):
    """Модель, представляющая координаты пользователя."""

    pass

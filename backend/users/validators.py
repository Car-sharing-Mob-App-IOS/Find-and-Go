from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
)
from django.utils.translation import gettext_lazy as _

from core.texts import MAX_NAME_SURNAME_LENGTH, MIN_NAME_SURNAME_LENGTH


def name_surname_validator(
    value,
    min_length=MIN_NAME_SURNAME_LENGTH,
    max_length=MAX_NAME_SURNAME_LENGTH,
):
    """Валидирует имя и фамилию."""
    validator = RegexValidator(
        regex=r"^[a-zA-Zа-яА-Я\-\–]+$",
        message=("Неверное значение, допускаются только буквы без пробелов."),
    )
    min_length_validator = MinLengthValidator(
        limit_value=min_length,
        message=f"Значение поля должно быть "
        f"длиной не менее {min_length} символов.",
    )

    max_length_validator = MaxLengthValidator(
        limit_value=max_length,
        message=f"Значение поля должно быть "
        f"длиной не более {max_length} символов.",
    )

    validator(value)
    min_length_validator(value)
    max_length_validator(value)


class MaximumLengthValidator(MinLengthValidator):
    """Класс для валидации длины пароля."""

    def __init__(self, max_length=18):
        self.max_length = max_length

    def validate(self, password, user=None):
        """Валидирует длину пароля."""
        if len(password) > self.max_length:
            raise ValidationError(
                _(
                    "Максимальная длина пароля - "
                    f"{self.max_length} символов."
                ),
                code="password_too_long",
                params={"max_length": self.max_length},
            )

    def get_help_text(self):
        """Возвращает текст справки о максимальной длине пароля."""
        return _("Максимальная длина пароля - " f"{self.max_length} символов.")

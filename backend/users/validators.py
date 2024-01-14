from core.texts import MAX_LENGTH_LAST_NAME
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils.translation import gettext_lazy as _


class MaxLengthLastNameValidator:
    """Класс для валидации длины фамилии."""

    def __init__(self, limit_value, message=None):
        self.limit_value = limit_value
        self.message = message

    def __call__(self, value):
        """Валидирует длину полученного значения."""
        if value and len(value) > self.limit_value:
            raise ValidationError(self.message, code='max_length', params={
                                  'limit_value': self.limit_value})


def name_surname_validator(value, min_length=3):
    """Валидирует имя и фамилию."""
    validator = RegexValidator(
        regex=r"^[a-zA-Zа-яА-Я\-\–]+$",  # Добавлены тире и дефис
        message=("Неверное значение, допускаются только буквы без пробелов."),
    )
    min_length_validator = MinLengthValidator(
        limit_value=min_length,
        message=f"Значение поля должно быть "
        f"длиной не менее {min_length} символов.",
    )

    max_length_validator = MaxLengthLastNameValidator(
        limit_value=MAX_LENGTH_LAST_NAME,
        message=f"Значение поля должно быть "
        f"длиной не более {MAX_LENGTH_LAST_NAME} символов.",
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
        return _(
            "Максимальная длина пароля - "
            f"{self.max_length} символов."
        )

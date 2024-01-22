from core.texts import (
    MAX_NAME_SURNAME_LENGTH,
    MIN_LENGTH_EMAIL,
    MIN_NAME_SURNAME_LENGTH,
    USER_EMAIL_LENGTH_MESSAGE,
)
from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
)
from django.utils.translation import gettext_lazy as _


def validate_email_min_length(value, email_min_length=MIN_LENGTH_EMAIL):
    """Валидирует длину email."""
    email_min_length_validator = MinLengthValidator(
        limit_value=email_min_length, message=USER_EMAIL_LENGTH_MESSAGE
    )
    email_min_length_validator(value)


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


class NamePasswordSimilarityValidator:
    """Валидатор схожести имени и фамилии с паролем."""

    def __init__(self, name_field='first_name', surname_field='last_name'):
        self.name_field = name_field
        self.surname_field = surname_field

    def validate(self, password, user=None):
        """Валидация имени и фамилии."""
        # Получаем имя и фамилию пользователя из объекта пользователя
        name = getattr(user, self.name_field, '')
        surname = getattr(user, self.surname_field, '')

        # Проверяем схожесть первых 7 символов имени или фамилии с паролем
        if (len(name) >= 7
                and password.lower().startswith(name[:7].lower())) or \
            (len(surname) >= 7
                and password.lower().startswith(surname[:7].lower())):
            raise ValidationError(
                _("Пароль слишком похож на имя или фамилию."),
                code='password_too_similar'
            )
